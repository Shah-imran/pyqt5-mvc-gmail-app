from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
import re

from apicalls.check_update import UpdateChecker
from apicalls.login import Login
from apicalls.registration import SignUp

from config import AppConfig, UserConfig, ConfigManager

from models.authentication_model import AuthenticationModel


def email_validation(email: str) -> bool:
    """

    @type email: str
    """
    # pass the regular expression
    # and the string in search() method
    if re.search(AppConfig.regex_for_email_validation, email):
        return True
    else:
        return False


class AuthenticationController(QObject):
    login_accepted = pyqtSignal()

    def __init__(self, model: AuthenticationModel):
        super().__init__()

        self._model = model

    @pyqtSlot(str)
    def change_updates_label_text(self, value: str) -> None:
        self._model.checking_updates_lbl_text = value

    @pyqtSlot(int)
    def change_progressbar_value(self, value: int) -> None:
        self._model.updates_progress_bar_value = value

    @pyqtSlot()
    def update_checked_value_change(self):
        self._model.update_checked = True

    @pyqtSlot(str)
    def update_sign_in_label(self, value: str) -> None:
        self._model.sign_in_label = value

    @pyqtSlot(str)
    def update_sign_up_label(self, value: str) -> None:
        self._model.sign_up_label = value

    def sign_up(self, email, password, confirm_password):
        password_match = password == confirm_password
        not_empty = email and password and len(password) >= 8
        valid_email = email_validation(email)

        if valid_email and password_match and not_empty:
            self._model.login_email = UserConfig.login_email = email
            self.sign_up_thread = SignUp(email, password)
            self.sign_up_thread.sign_up_successful.connect(self.update_sign_up_label)
            self.sign_up_thread.sign_up_failed.connect(self.update_sign_up_label)
            self.sign_up_thread.finished.connect(self.sign_up_thread.quit)
            self.sign_up_thread.finished.connect(self.sign_up_thread.deleteLater)
            self.sign_up_thread.start()
        else:
            self.update_sign_up_label("Must be a valid email.\n" +
                                      "Fields can't be empty\n" +
                                      "and Passwords should be same.")

    def login(self, email, password):
        self._model.login_email = UserConfig.login_email = email
        self.login_thread = Login(email, password)
        self.login_thread.login_successful.connect(self.login_accepted.emit)
        self.login_thread.login_failed.connect(self.update_sign_in_label)
        self.login_thread.finished.connect(self.login_thread.quit)
        self.login_thread.finished.connect(self.login_thread.deleteLater)
        self.login_thread.start()

    def checking_for_update(self):
        self.update_checker = UpdateChecker()
        self.update_checker.label_update.connect(self.change_updates_label_text)
        self.update_checker.progressbar_update.connect(self.change_progressbar_value)
        self.update_checker.update_checked.connect(self.update_checked_value_change)
        self.update_checker.finished.connect(self.update_checker.quit)
        self.update_checker.finished.connect(self.update_checker.deleteLater)
        self.update_checker.start()

    def load_config(self):
        self.config_manager = ConfigManager('load')
        self.config_manager.loading_finished.connect(self.update_login_email)
        self.config_manager.finished.connect(self.config_manager.quit)
        self.config_manager.finished.connect(self.config_manager.deleteLater)
        self.config_manager.start()

    @pyqtSlot()
    def update_login_email(self):
        self._model.login_email = UserConfig.login_email

    def demo_thread(self):
        print("finished")
        # self.thread = QThread()
        # self.uc = UpdateChecker()
        # self.uc.label_update.connect(self.change_updates_label_text)
        # self.uc.progressbar_update.connect(self.change_progressbar_value)
        # self.uc.moveToThread(self.thread)
        # self.thread.started.connect(self.uc.run)
        # self.uc.finished.connect(self.thread.quit)
        # self.uc.finished.connect(self.uc.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # self.thread.start()
        pass
