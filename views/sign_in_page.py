from PyQt5 import QtWidgets, QtGui
from views.generated.sign_in_screen import Ui_LoginScreen
from views.frameless_screen import FramelessScreen


class SignInScreen(Ui_LoginScreen, QtWidgets.QWidget):
    def __init__(self):
        super(SignInScreen, self).__init__()
        self.setupUi(self)
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.notification_message_lbl.setVisible(True)

    def clear(self):
        self.password_lin.resizeEvent(None)
        self.password_lin.setText("")
        self.email_lin.setText("")
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)


if __name__ == "__main__":
    from assets import utils
    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = SignInScreen()
    screen.show()
    app.setStyleSheet(utils.load_app_style())
    app.exec_()
