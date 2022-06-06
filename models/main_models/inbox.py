from PyQt5.QtCore import QObject, pyqtSignal
from config import UserConfig
import pandas as pd
import queue


class InboxModel(QObject):
    date_changed = pyqtSignal(str)
    dialog_label_text_changed = pyqtSignal(str)
    dialog_progressbar_value_changed = pyqtSignal(float)
    change_new_email_count = pyqtSignal(int)
    to_email_lbl_changed = pyqtSignal(str)
    from_email_lbl_changed = pyqtSignal(str)
    email_topic_lbl_changed = pyqtSignal(str)
    email_body_changed = pyqtSignal(str)
    email_body_font_size_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self._date = ''
        self._group = 'group_a'
        self._alphabetical_sort = 'a-z'     # a -z or z - a
        self._date_sort = 'Earliest'    # Earliest either Latest
        self._email_in_view_uid = ''
        self._dialog_label_text = ''
        self._dialog_progressbar_value = float(0)
        self.download_running = False
        self._inbox_data_df = pd.DataFrame()
        self._inbox_queue = queue.Queue()
        self._new_email_count = 0
        self._to_email_lbl = ""
        self._from_email_lbl = ""
        self._email_topic_lbl = ""
        self._email_body = ""
        self._email_body_font_size = 12
        
    @property
    def email_body_font_size(self) -> int:
        return self._email_body_font_size
    
    @email_body_font_size.setter
    def email_body_font_size(self, value: int):
        self.email_body_font_size_changed.emit(value)
        self._email_body_font_size = value
        
    @property
    def email_in_view_uid(self) -> str:
        return self._email_in_view_uid
    
    @email_in_view_uid.setter
    def email_in_view_uid(self, value: str):
        self._email_in_view_uid = value
        
    @property
    def email_body(self) -> str:
        return self._email_body
    
    @email_body.setter
    def email_body(self, value: str):
        self.email_body_changed.emit(value)
        self._email_body = value
        
    @property
    def email_topic_lbl(self) -> str:
        return self._email_topic_lbl
    
    @email_topic_lbl.setter
    def email_topic_lbl(self, value: str):
        self.email_topic_lbl_changed.emit(value)
        self._email_topic_lbl = value    
    
    @property
    def from_email_lbl(self) -> str:
        return self._from_email_lbl
    
    @from_email_lbl.setter
    def from_email_lbl(self, value: str):
        self.from_email_lbl_changed.emit(value)
        self._from_email_lbl = value
        
    @property
    def to_email_lbl(self) -> str:
        return self._to_email_lbl
    
    @to_email_lbl.setter
    def to_email_lbl(self, value: str):
        self.to_email_lbl_changed.emit(value)
        self._to_email_lbl = value
        
    @property
    def new_email_count(self) -> int:
        return self._new_email_count
    
    @new_email_count.setter
    def new_email_count(self, value: int):
        self.change_new_email_count.emit(value)
        self._new_email_count = value
        
    @property
    def inbox_queue(self) -> queue.Queue:
        return self._inbox_queue
    
    @inbox_queue.setter
    def inbox_queue(self, value: queue.Queue):
        self._inbox_queue = value
        
    @property
    def inbox_data_df(self) -> pd.DataFrame:
        return self._inbox_data_df

    @inbox_data_df.setter
    def inbox_data_df(self, value: pd.DataFrame):
        self._inbox_data_df = value
        
    @property
    def dialog_label_text(self) -> str:
        return self._dialog_label_text
    
    @dialog_label_text.setter
    def dialog_label_text(self, value: str):
        self.dialog_label_text_changed.emit(value)
        self._dialog_label_text = value
        
    @property
    def dialog_progressbar_value(self) -> float:
        return self._dialog_progressbar_value
    
    @dialog_progressbar_value.setter
    def dialog_progressbar_value(self, value: float):
        self.dialog_progressbar_value_changed.emit(value)
        self._dialog_progressbar_value = value

    @property
    def date_sort(self):
        return self._date_sort

    @date_sort.setter
    def date_sort(self, value):
        self._date_sort = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    @property
    def alphabetical_sort(self):
        return self._alphabetical_sort

    @alphabetical_sort.setter
    def alphabetical_sort(self, value):
        self._alphabetical_sort = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        UserConfig.imap_date = value
        self.date_changed.emit(value)
        self._date = value
