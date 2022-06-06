from PyQt5 import QtWidgets
from views.generated.sign_up_screen import Ui_SignUp
from views.frameless_screen import FramelessScreen


class SignUpScreen(QtWidgets.QWidget, Ui_SignUp):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        self.setupUi(self)
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.notification_message_lbl.setVisible(True)


    def clear(self):
        self.password_lin.setText("")
        self.confirm_password_lin.setText("")
        self.email_lin.setText("")
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_lin.setEchoMode(QtWidgets.QLineEdit.Password)


if __name__ == "__main__":
    from assets import utils
    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = SignUpScreen()
    screen.show()
    app.setStyleSheet(utils.load_app_style())
    app.exec_()
