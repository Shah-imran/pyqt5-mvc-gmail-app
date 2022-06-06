from PyQt5.QtCore import QObject, pyqtSignal


class AuthenticationModel(QObject):
    checking_updates_lbl_changed = pyqtSignal(str)
    updates_progress_bar_value_changed = pyqtSignal(int)
    sign_in_label_changed = pyqtSignal(str)
    sign_up_label_changed = pyqtSignal(str)
    login_email_changed = pyqtSignal(str)

    @property
    def checking_updates_lbl_text(self) -> str:
        return self._checking_updates_lbl_text

    @checking_updates_lbl_text.setter
    def checking_updates_lbl_text(self, value: str) -> None:
        self._checking_updates_lbl_text = value
        self.checking_updates_lbl_changed.emit(value)

    @property
    def updates_progress_bar_value(self) -> int:
        return self._updates_progress_bar_value

    @updates_progress_bar_value.setter
    def updates_progress_bar_value(self, value: int) -> None:
        self._updates_progress_bar_value = value
        self.updates_progress_bar_value_changed.emit(value)

    @property
    def sign_in_label(self) -> int:
        return self._sign_in_label

    @sign_in_label.setter
    def sign_in_label(self, value: int) -> None:
        self._sign_in_label = value
        self.sign_in_label_changed.emit(value)

    @property
    def sign_up_label(self) -> int:
        return self._sign_up_label

    @sign_up_label.setter
    def sign_up_label(self, value: int) -> None:
        self._sign_up_label = value
        self.sign_up_label_changed.emit(value)

    @property
    def login_email(self) -> str:
        return self._login_email

    @login_email.setter
    def login_email(self, value: str) -> None:
        self._login_email = value
        self.login_email_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._checking_updates_lbl_text = ''
        self._updates_progress_bar_value = 30
        self._sign_in_label = ''
        self._sign_up_label = ''
        self.update_checked = False
        self._login_email = ''
