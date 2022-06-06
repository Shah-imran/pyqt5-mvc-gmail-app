from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtWidgets import QMessageBox
from db.database import Database
from models.main_model import MainModel
from downloadmail import download
from downloadmail.imap.imap import ImapSetReadFlag
from config import UserConfig, AppConfig, logger
from .popup import PopUp
import pandas as pd
import traceback
import queue


class InboxController(QObject):
    show_download_dialog = pyqtSignal()
    change_download_dialog_button_text = pyqtSignal(str)
    close_download_dialog = pyqtSignal()
    spinner_control = pyqtSignal(str)
    stop_download = pyqtSignal()
    initialize_inbox_table = pyqtSignal()
    add_row_to_inbox_table = pyqtSignal(object)
    update_checked_email = pyqtSignal(str)
    open_email = pyqtSignal(str)

    def __init__(self, model: MainModel, db: Database):
        super().__init__()

        self._db = db
        self._model = model

        self.add_row_timer = QTimer()
        self.add_row_timer.setInterval(10)
        self.add_row_timer.timeout.connect(self.inbox_queue_processor)
        self.popup = PopUp()

    @pyqtSlot(bool)
    def set_email_body_font_size(self, value: bool):
        if value:
            self._model.inbox_model.email_body_font_size += 1
        else:
            if self._model.inbox_model.email_body_font_size > AppConfig.inbox_page_email_body_font_size_min:
                self._model.inbox_model.email_body_font_size -= 1

    def update_new_email_count(self, value: int):
        self._model.inbox_model.new_email_count = value

    @pyqtSlot(str)
    def update_imap_date(self, value):
        self._model.inbox_model.date = value

    @pyqtSlot(bool)
    def update_group_selection(self, value):
        if value:
            self._model.inbox_model.group = 'group_a'
        else:
            self._model.inbox_model.group = 'group_b'

    def finish_sorting_inbox(self):
        self.add_row_timer.start()

    def sort_inbox_data(self, option: str):
        if len(self._model.inbox_model.inbox_data_df) > 0:
            self.initialize_inbox_table.emit()
            self.spinner_control.emit("inbox_screen")

            self.sort_inbox = SortInbox(self._model, option)
            self.sort_inbox.finished.connect(self.sort_inbox.quit)
            self.sort_inbox.finished.connect(self.sort_inbox.deleteLater)
            self.sort_inbox.finished.connect(self.finish_sorting_inbox)
            self.sort_inbox.start()
        else:
            self.popup.warning("No Data in Inbox")

    @pyqtSlot(bool)
    def update_alphabetical_sort(self, value):
        if value:
            self._model.inbox_model.alphabetical_sort = 'a-z'
        else:
            self._model.inbox_model.alphabetical_sort = 'z-a'

        self.sort_inbox_data(self._model.inbox_model.alphabetical_sort)

    @pyqtSlot(bool)
    def update_date_sort(self, value):
        if value:
            self._model.inbox_model.date_sort = 'Earliest'
        else:
            self._model.inbox_model.date_sort = 'Latest'

        self.sort_inbox_data(self._model.inbox_model.date_sort)

    @pyqtSlot()
    def confirmation_window_for_download(self):
        confirmation_window = QMessageBox()
        result = confirmation_window.question(None, "Confirmation Window",
                                              "Are you sure?",
                                              confirmation_window.Ok | confirmation_window.Cancel)

        if result == confirmation_window.Ok:
            self.imap_download()

    @pyqtSlot(object)
    def update_inbox_data(self, data_queue: queue.Queue):
        self._model.inbox_model.inbox_data_df = pd.DataFrame()
        self._model.inbox_model.inbox_queue = data_queue
        self.initialize_inbox_table.emit()
        self.spinner_control.emit("inbox_screen")
        self.add_row_timer.start()

    @pyqtSlot(object)
    def update_progress_info(self, info: dict):
        self._model.inbox_model.dialog_label_text = f"Total Email Downloaded : {info['total_email_downloaded']} " \
                                                    f"Finished : {info['account_finished']} " \
                                                    f"Failed: {info['email_failed']}"
        self._model.inbox_model.dialog_progressbar_value = (info['account_finished'] / info['total_account']) * 100

    @pyqtSlot(bool)
    def set_download_status(self, value):
        self._model.inbox_model.download_running = value
        if not value:
            self.spinner_control.emit(None)

    @pyqtSlot(str)
    def wrap_up_downloading(self, value: str):
        self.change_download_dialog_button_text.emit(value)
        self.spinner_control.emit(None)

    @pyqtSlot(str)
    def download_dialog_button_action(self, value: str):
        """
        this method is only for button
        """
        if value == "CANCEL":
            # wait for all the processes to finish then emit a signal to change the button text
            self.stop_download.emit()
            # self.change_download_dialog_button_text.emit()
        else:
            if not self._model.inbox_model.download_running:
                self.close_download_dialog.emit()
            else:
                self.spinner_control.emit("inbox_screen")

    @pyqtSlot()
    def close_all_download_processes(self):
        """
        this is only when someone clicks on cross on dialog
        """
        if self._model.inbox_model.download_running:
            self.stop_download.emit()
            self.spinner_control.emit("inbox_screen")
        # close all download threads safely

    def imap_download(self):
        group = self._model.database_model.group_a.copy() if self._model.inbox_model.group == "group_a" \
                else self._model.database_model.group_b.copy()

        if len(group) > 0:
            kwargs = {
                "group": group,
                "imap_date": self._model.inbox_model.date,
                "limit_of_thread": UserConfig.limit_of_thread
            }

            self.wrap_up_downloading("CANCEL")

            self.imap_download_thread = download.DownloadThreadStarter(**kwargs)
            self.imap_download_thread.thread_quit.connect(lambda: self.wrap_up_downloading("CLOSE"))
            self.imap_download_thread.finished.connect(self.imap_download_thread.quit)
            self.imap_download_thread.finished.connect(self.imap_download_thread.deleteLater)
            self.imap_download_thread.change_download_status.connect(self.set_download_status)
            self.imap_download_thread.update_progress_info.connect(self.update_progress_info)
            self.imap_download_thread.update_inbox_data.connect(self.update_inbox_data)
            self.stop_download.connect(self.imap_download_thread.close)
            self.imap_download_thread.start()
            self.show_download_dialog.emit()

        else:
            alert = QMessageBox()
            alert.warning(None, "Warning", "No data in selected group")

    @pyqtSlot(str, bool)
    def mark_email(self, uid: str, state: bool):
        row = self._model.inbox_model.inbox_data_df.loc[
            self._model.inbox_model.inbox_data_df['uuid'] == uid].index
        self._model.inbox_model.inbox_data_df['checkbox_status'][row] = state

    def set_read_flag(self, data: dict):
        data['imap_server'] = AppConfig.imap_server
        data['imap_port'] = AppConfig.imap_port
        imap_set_read_flag = ImapSetReadFlag(**data)
        imap_set_read_flag.start()

    @pyqtSlot(str, int)
    def open_email(self, uid: str, table_row: int):
        row = self._model.inbox_model.inbox_data_df.loc[
            self._model.inbox_model.inbox_data_df['uuid'] == uid].index

        current_email_data = self._model.inbox_model.inbox_data_df.loc[row].to_dict('records')[0]

        if self._model.inbox_model.inbox_data_df['flag'][row].item() == "UNSEEN":
            self._model.inbox_model.inbox_data_df['flag'][row] = "SEEN"
            current_email_data['row'] = table_row
            current_email_data['flag'] = "SEEN"
            self.add_row_to_inbox_table.emit(current_email_data)
            self.set_read_flag(current_email_data)

        self._model.inbox_model.email_in_view_uid = uid
        self._model.inbox_model.to_email_lbl = current_email_data['to_mail']
        self._model.inbox_model.from_email_lbl = current_email_data['from_mail']
        self._model.inbox_model.email_topic_lbl = current_email_data['subject']
        self._model.inbox_model.email_body = current_email_data['body']

    def pandas_convert_dtypes(self):
        self._model.inbox_model.inbox_data_df['proxy_port'] = \
            self._model.inbox_model.inbox_data_df['proxy_port'].astype(int)
        self._model.inbox_model.inbox_data_df['checkbox_status'] = \
            self._model.inbox_model.inbox_data_df['checkbox_status'].astype(bool)

    def inbox_queue_processor(self):
        try:
            count = 0

            while not self._model.inbox_model.inbox_queue.empty():
                if count == 2:
                    break

                row = self._model.inbox_model.inbox_queue.get()
                self.add_row_to_inbox_table.emit(row)
                self._model.inbox_model.inbox_data_df = self._model.inbox_model.inbox_data_df.\
                    append(row, ignore_index=True)
                self.pandas_convert_dtypes()
                self.update_new_email_count(len(self._model.inbox_model.inbox_data_df))

            else:
                self.spinner_control.emit(None)
                self.add_row_timer.stop()

        except Exception as e:
            logger.error(f"Error at inbox_queue_processor: {e}\n{traceback.format_exc()}")

            self.spinner_control.emit(None)
            self.add_row_timer.stop()

    def select_all(self):
        self._model.inbox_model.inbox_data_df['checkbox_status'] = 1

    def initiate_deleting_process(self, event):
        temp_df = self._model.inbox_model.inbox_data_df.copy()
        temp_df = temp_df.loc[temp_df['checkbox_status'] == 1]

        if temp_df.shape[0] > 0:
            self.spinner_control.emit("inbox_screen")
            SortInbox(self._model, None).reset_email_in_view_models()

            self.delete_thread = Delete(self._model, temp_df)

            self.delete_thread.finished.connect(lambda: self.spinner_control.emit(None))
            self.delete_thread.start()
        else:
            self.popup.warning("You have to select something first")


class Delete(QThread):
    def __init__(self, model: MainModel, df: pd.DataFrame):
        super(Delete, self).__init__()

        self._model = model
        self.df = df

    def run(self) -> None:
        logger.info(f"Starting {self.__class__.__name__}")


        logger.info(f"Finished {self.__class__.__name__}")


class SortInbox(QThread):
    def __init__(self, model: MainModel, option: str):
        super(SortInbox, self).__init__()

        self._model = model
        self._option = option

    def run(self) -> None:
        logger.info(f"Starting {self.__class__.__name__}...{self._option}")

        self.reset_email_in_view_models()
        inbox_data_df = self._model.inbox_model.inbox_data_df.copy()
        self._model.inbox_model.inbox_data_df = pd.DataFrame()

        if self._option == "Latest":
            inbox_data_df.sort_values(by="date", inplace=True, ascending=True)
        elif self._option == "a-z":
            inbox_data_df.sort_values(by="subject", inplace=True, ascending=False)
        elif self._option == "z-a":
            inbox_data_df.sort_values(by="subject", inplace=True, ascending=True)
        else:
            inbox_data_df.sort_values(by="date", inplace=True, ascending=False)

        inbox_data_df.reset_index(drop=True, inplace=True)
        inbox_data_dict = inbox_data_df.to_dict("records")

        for index, item in enumerate(inbox_data_dict):
            self._model.inbox_model.inbox_queue.put(item.copy())

        logger.info(f"Finished {self.__class__.__name__}...{self._option}")

    def reset_email_in_view_models(self):
        self._model.inbox_model.email_in_view_uid = ''
        self._model.inbox_model.to_email_lbl = ''
        self._model.inbox_model.from_email_lbl = ''
        self._model.inbox_model.email_topic_lbl = ''
        self._model.inbox_model.email_body = ''
