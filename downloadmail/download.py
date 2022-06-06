from downloadmail.imap.imap import ImapDownload
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal, QTimer
from config import AppConfig, logger
from threading import Thread
import time
import traceback


class DownloadThreadStarter(QThread):
    change_download_status = pyqtSignal(bool)
    update_progress_info = pyqtSignal(object)
    update_inbox_data = pyqtSignal(object)
    thread_quit = pyqtSignal()

    def __init__(self, **kwargs):
        super(DownloadThreadStarter, self).__init__()

        self.stop_download = False
        self.proxy_type = AppConfig.proxy_type
        self.imap_server = AppConfig.imap_server
        self.imap_port = AppConfig.imap_port

        self.group = kwargs['group']
        self.total_account = len(self.group)
        self.imap_date = kwargs["imap_date"]
        self.limit_of_thread = kwargs['limit_of_thread']

        # self.progressbar_update_timer = QTimer()
        # self.progressbar_update_timer.setInterval(100)
        # self.progressbar_update_timer.timeout.connect(self.progressbar_update_slot)
        # self.progressbar_update_thread = Thread(target=self.progressbar_update_slot, daemon=True)

        # Initialize ImapDownload class variable
        ImapDownload.thread_open = 0
        ImapDownload.stop_download = False
        ImapDownload.total_email_downloaded = 0
        with ImapDownload.email_q.mutex:
            ImapDownload.email_q.queue.clear()
        ImapDownload.email_failed = 0
        ImapDownload.account_finished = 0

    def progressbar_update_slot(self):
        self.update_progress_info.emit({
            "total_email_downloaded": ImapDownload.total_email_downloaded,
            "email_failed": ImapDownload.email_failed,
            "account_finished": ImapDownload.account_finished,
            "total_account": self.total_account
        })

    def close(self):
        self.stop_download = True
        ImapDownload.stop_download = True

    def run(self) -> None:
        try:
            logger.info("Starting Imap Download...")

            self.change_download_status.emit(True)
            self.progressbar_update_slot()

            list_of_thread_class = []

            for index, item in self.group.iterrows():
                if self.stop_download:
                    break

                proxy_type = self.proxy_type
                proxy_user = item["PROXY_USER"]
                proxy_pass = item["PROXY_PASS"]
                imap_user = item["EMAIL"]
                imap_pass = item["EMAIL_PASS"]
                first_from_name = item["FIRSTFROMNAME"]
                last_from_name = item["LASTFROMNAME"]

                if item["PROXY:PORT"] != " ":
                    proxy_host = item["PROXY:PORT"].split(':')[0]
                    proxy_port = int(item["PROXY:PORT"].split(':')[1])
                else:
                    proxy_host = ""
                    proxy_port = ""

                imap_data = {
                    "proxy_type": proxy_type,
                    "proxy_user": proxy_user,
                    "proxy_pass": proxy_pass,
                    "proxy_host": proxy_host,
                    "proxy_port": proxy_port,
                    "user": imap_user,
                    "pass": imap_pass,
                    "imap_server": self.imap_server,
                    "imap_port": self.imap_port,
                    "imap_date": self.imap_date,
                    "first_from_name": first_from_name,
                    "last_from_name": last_from_name
                }

                while ImapDownload.thread_open >= self.limit_of_thread and not self.stop_download:
                    self.progressbar_update_slot()
                    time.sleep(0.1)

                imap_download = ImapDownload(**imap_data)
                imap_download.start()
                list_of_thread_class.append(imap_download)

            while ImapDownload.thread_open != 0:
                self.progressbar_update_slot()
                time.sleep(0.1)

            self.progressbar_update_slot()

        except Exception as e:
            logger.error(f"Error at {self.__class__.__name__}: {e}\n{traceback.format_exc()}")

        finally:
            logger.info("Imap Download Done.")
            self.change_download_status.emit(False)
            self.thread_quit.emit()

            if not ImapDownload.email_q.empty():
                self.update_inbox_data.emit(ImapDownload.email_q)
