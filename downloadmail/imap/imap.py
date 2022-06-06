import imaplib
import codecs
import email
import queue
import traceback

from datetime import datetime, timedelta, timezone
from PyQt5.QtCore import QThread
from threading import Thread
import uuid

from downloadmail.imap import proxy_imap
from config import AppConfig, logger


def difference_between_time(first_time, last_time):
    difference = last_time - first_time
    seconds_in_day = 24 * 60 * 60
    minutes, seconds = divmod(
        difference.days * seconds_in_day + difference.seconds, 60)
    elapsed_time = round(minutes + (seconds / 60), 2)
    return elapsed_time


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def slashescape(err):
    """ codecs error handler. err is UnicodeDecode instance. return
    a tuple with a replacement for the unencodable part of the input
    and a position where encoding should continue"""
    # print err, dir(err), err.start, err.end, err.object[:err.start]
    thebyte = err.object[err.start:err.end]
    repl = u'\\x' + hex(ord(thebyte))[2:]
    return (repl, err.end)


codecs.register_error('slashescape', slashescape)


class ImapBase:
    def __init__(self, **kwargs):
        super().__init__()
        self._proxy_host = kwargs["proxy_host"]
        self._proxy_port = kwargs["proxy_port"]
        self._proxy_type = kwargs["proxy_type"]
        self._proxy_user = kwargs["proxy_user"]
        self._proxy_pass = kwargs["proxy_pass"]
        self._imap_host = kwargs["imap_server"]
        self._imap_port = kwargs["imap_port"]
        self._imap_user = kwargs["user"]
        self._imap_pass = kwargs["pass"]

    def _login(self):
        if self._proxy_host != "":
            imap = proxy_imap.IMAP(proxy_host=self._proxy_host, proxy_port=self._proxy_port,
                                   proxy_type=self._proxy_type,
                                   proxy_user=self._proxy_user, proxy_pass=self._proxy_pass, host=self._imap_host,
                                   port=self._imap_port, timeout=30)
        else:
            imap = imaplib.IMAP4_SSL(self._imap_host)

        imap.login(self._imap_user, self._imap_pass)

        return imap


class ImapCheckForBlocks(ImapBase):
    def __init__(self, **kwargs):
        self._time_limit = kwargs["time_limit"]
        super().__init__(**kwargs)

    def check_for_block_messages(self):
        try:
            # FROM - Mail Delivery Subsystem mailer-daemon@googlemail.com
            # SUBJECT - Delivery Status Notification (Failure)
            # Message bloqué   or  Message blocked

            imap = self._login()
            imap.select("Inbox", readonly=True)

            date = datetime.today() - timedelta(days=1)

            tmp, data = imap.search(
                None,
                f'(SINCE "{date.strftime("%d-%b-%Y")}" SUBJECT "Delivery Status Notification (Failure)"' +
                'FROM "mailer-daemon@googlemail.com")')

            for num in data[0].split():
                tmp, data = imap.fetch(num, '(UID RFC822)')

                email_message = email.message_from_string(
                    data[0][1].decode('utf-8', 'slashescape'))

                date = email.utils.parsedate_to_datetime(email_message['Date'])
                difference_in_minute = difference_between_time(
                    date, datetime.now(timezone.utc))

                if difference_in_minute < self._time_limit:
                    b = email_message
                    body = ""

                    if b.is_multipart():
                        for part in b.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            # skip any text/plain (txt) attachments
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
                    else:
                        body = b.get_payload(decode=True)

                    try:
                        body = body.decode("utf-8", 'slashescape')
                    except:
                        body = body

                    blocked_message_keyword = [
                        "Message bloqué", "Message blocked", "Message rejected"]

                    for item in blocked_message_keyword:
                        if item.lower() in body.lower():
                            return True

            return False

        except Exception as e:
            logger.error(
                f"Error at {self.__class__.__name__}.check_for_block_messages - {self._imap_user} - {e}")
            return False


class DeleteEmail(ImapBase, Thread):
    def __init__(self, **kwargs):
        super(DeleteEmail, self).__init__(**kwargs)

    def run(self) -> None:
        pass


class ImapSetReadFlag(ImapBase, Thread):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setDaemon(True)
        self._uid = kwargs['uid']

    def run(self) -> None:
        try:
            logger.info(f"Starting {self.__class__.__name__} {self._imap_user} - {self._uid}")
            imap = self._login()

            imap.select("Inbox")

            imap.uid('STORE', self._uid, '+FLAGS', '\Seen')
            imap.close()
            imap.logout()
            logger.info(f"Ending {self.__class__.__name__} {self._imap_user} - {self._uid}")

        except Exception as e:
            logger.error(f"Error at {self.__class__.__name__}: {e}\n"
                         f"format_exec: {traceback.format_exc()}")
        finally:
            pass


class ImapDownload(ImapBase, Thread):
    thread_open = 0
    stop_download = False
    total_email_downloaded = 0
    email_q = queue.Queue()
    email_failed = 0
    account_finished = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._first_from_name = kwargs['first_from_name']
        self._last_from_name = kwargs['last_from_name']
        self._imap_date = kwargs['imap_date']
        self.setDaemon(True)

    def run(self):
        try:
            ImapDownload.thread_open += 1
            imap = self._login()

            imap.select("Inbox", readonly=True)

            objDate = datetime.strptime(self._imap_date, '%m/%d/%Y')
            offset_naive_date = objDate
            offset_aware_date = utc_to_local(offset_naive_date)

            for item in ['UNSEEN', 'SEEN']:

                tmp, data = imap.search(None, '({} SINCE "{}")'.format(
                    item, objDate.strftime('%d-%b-%Y')))

                for num in data[0].split():
                    if ImapDownload.stop_download:
                        break
                    tmp, data = imap.fetch(num, '(UID RFC822)')
                    raw = data[0][0]
                    raw_str = raw.decode("utf-8")
                    uid = raw_str.split()[2]
                    email_message = email.message_from_string(
                        data[0][1].decode('utf-8', 'slashescape'))
                    # print(email_message.items())
                    b = email_message
                    body = ""

                    if b.is_multipart():
                        for part in b.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            # skip any text/plain (txt) attachments
                            if (ctype == 'text/plain' or ctype == 'text/html') and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
                    else:
                        body = b.get_payload(decode=True)

                    try:
                        body = body.decode("utf-8", 'ignore')
                    except:
                        # print(body)
                        body = body

                    subject = email.header.make_header(
                        email.header.decode_header(email_message['Subject']))

                    subject = str(subject)

                    from_name = str(email.header.make_header(email.header.
                        decode_header(
                        email.utils.parseaddr(email_message['From'])[0])))
                    from_mail = str(email.header.make_header(email.header.
                        decode_header(
                        email.utils.parseaddr(email_message['From'])[1])))

                    to_name = str(email.header.make_header(email.header.
                        decode_header(
                        email.utils.parseaddr(email_message['To'])[0])))
                    to_mail = str(email.header.make_header(email.header.
                        decode_header(
                        email.utils.parseaddr(email_message['To'])[1])))
                    mail_date = email.utils.parsedate_to_datetime(
                        email_message['Date'])

                    t_dict = {
                        'uuid': str(uuid.uuid4()),
                        'checkbox_status': False,
                        'uid': uid,
                        'to': "{} {}".format(to_name, to_mail),
                        'TONAME': to_name,
                        'to_mail': to_mail,
                        'message-id': email.utils.parseaddr(email_message['Message-ID'])[1],
                        'from': "{} {}".format(from_name, from_mail),
                        'from_name': from_name,
                        'from_mail': from_mail,
                        'date': utc_to_local(mail_date),
                        'subject': subject,
                        'user': self._imap_user,
                        'pass': self._imap_pass,
                        'body': body,
                        'proxy_host': self._proxy_host,
                        'proxy_port': self._proxy_port,
                        'proxy_user': self._proxy_user,
                        'proxy_pass': self._proxy_pass,
                        'proxy_type': self._proxy_type,
                        'first_from_name': self._first_from_name,
                        'last_from_name': self._last_from_name,
                        'flag': item,
                        'Webhook_flag': False  # means not fired yet

                    }

                    # # print(from_name, from_mail, to_name, to_mail, subject, body)
                    # print("utc - ", utc_to_local(mail_date),
                    #       "| Non utc - ", mail_date)

                    try:
                        if mail_date.tzinfo:
                            print("Date is offset aware.")

                            if offset_aware_date <= mail_date:
                                t_dict['date'] = utc_to_local(mail_date)
                                ImapDownload.email_q.put(t_dict.copy())
                                ImapDownload.total_email_downloaded += 1
                            else:
                                print("From previous date.")
                        else:
                            print("Date is offset naive.")

                            if offset_naive_date <= mail_date:
                                t_dict['date'] = utc_to_local(mail_date)
                                ImapDownload.email_q.put(t_dict.copy())
                                ImapDownload.total_email_downloaded += 1
                            else:
                                print("From previous date offset naive.")

                    except Exception as e:
                        logger.error(
                            f"Error on Imap download {self._imap_user} : {traceback.format_exc()}")

            imap.close()
            imap.logout()
        except Exception as e:
            ImapDownload.email_failed += 1
            logger.error(
                f"Error at {self.__class__.__name__} - {self._imap_user}\n{traceback.format_exc()}")
        finally:
            ImapDownload.account_finished += 1
            ImapDownload.thread_open -= 1
