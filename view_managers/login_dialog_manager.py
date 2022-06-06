from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from views.login_stacked import LoginStackedWidgetDialog
from config import UserConfig


class LoginDialogManager(LoginStackedWidgetDialog):
    login_accepted = pyqtSignal()

    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller

        # connect your models signals here
        self._model.checking_updates_lbl_changed.connect(self.on_updates_lbl_change)
        self._model.updates_progress_bar_value_changed.connect(self.on_progressbar_value_change)
        self._model.sign_in_label_changed.connect(self.update_sign_in_label)
        self._model.sign_up_label_changed.connect(self.update_sign_up_label)


        # gui signals here
        self._model.login_email_changed.connect(self.update_login_email)
        self.login_accepted.connect(self.handle_login)
        self.first_page.login_btn.clicked.connect(
            self.handle_switch_to_login_window
        )
        self.first_page.signup_btn.clicked.connect(
            self.handle_switch_to_signup_window
        )
        self.login_screen.back.clicked.connect(
            self.handle_switch_to_first_page
        )
        self.signup_screen.back.clicked.connect(
            self.handle_switch_to_first_page
        )
        self.login_screen.login_btn.clicked.connect(
            lambda: self._main_controller.login(
                self.login_screen.email_lin.text().strip(),
                self.login_screen.password_lin.text())
        )
        self.signup_screen.signup_btn.clicked.connect(
            lambda: self._main_controller.sign_up(
                self.signup_screen.email_lin.text().strip(),
                self.signup_screen.password_lin.text(),
                self.signup_screen.confirm_password_lin.text()
            )
        )

    @pyqtSlot(str)
    def update_login_email(self, value):
        self.login_screen.email_lin.setText(value)

    @pyqtSlot()
    def handle_login(self):
        self.accept()

    @pyqtSlot(str)
    def update_sign_in_label(self, value):
        self.login_screen.notification_message_lbl.setText(value)

    @pyqtSlot(str)
    def update_sign_up_label(self, value):
        self.signup_screen.notification_message_lbl.setText(value)

    @pyqtSlot(str)
    def on_updates_lbl_change(self, value):
        self.first_page.checking_updates_lbl.setText(value)

    @pyqtSlot(int)
    def on_progressbar_value_change(self, value):
        self.first_page.updates_progress_bar.setValue(value)

    def handle_switch_to_login_window(self):
        if self._model.update_checked:
            # this clear all the fields in the page
            # self.login_screen.clear()
            self.stacked_pages.setCurrentIndex(1)

    def handle_switch_to_signup_window(self):
        self.signup_screen.clear()
        self.stacked_pages.setCurrentIndex(2)

    def handle_switch_to_first_page(self):
        self.stacked_pages.setCurrentIndex(0)


if __name__ == "__main__":
    from assets import utils

    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    login_dialog = LoginDialogManager()
    login_dialog.exec_()
