from PyQt5 import QtWidgets
from assets import utils
from views.frameless_screen import FramelessScreen
from views.first_screen_page import FirstScreen
from views.sign_in_page import SignInScreen
from views.sign_up_page import SignUpScreen


class LoginStackedWidgetDialog(FramelessScreen):
    def __init__(self):
        super(LoginStackedWidgetDialog, self).__init__()
        self.stacked_pages = QtWidgets.QStackedWidget()
        self.first_page = FirstScreen()
        self.login_screen = SignInScreen()
        self.signup_screen = SignUpScreen()
        self.stacked_pages.addWidget(self.first_page)
        self.stacked_pages.addWidget(self.login_screen)
        self.stacked_pages.addWidget(self.signup_screen)
        self.set_central_widget(self.stacked_pages)
        self.stacked_pages.setCurrentIndex(0)
        self.setStyleSheet(utils.load_app_style())




