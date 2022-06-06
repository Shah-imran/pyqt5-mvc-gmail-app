from PyQt5 import QtWidgets
from views.generated.first_screen import Ui_FirstScreen
from views.frameless_screen import FramelessScreen


class FirstScreen(QtWidgets.QWidget, Ui_FirstScreen):
    def __init__(self):
        super(FirstScreen, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    from assets import utils
    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = FirstScreen()
    screen.show()
    app.setStyleSheet(utils.load_app_style())
    app.exec_()
