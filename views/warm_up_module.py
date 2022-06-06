from enum import Enum
from PyQt5 import QtWidgets, QtGui, QtCore
from views.generated.warm_up_module import Ui_MainWindow


class EmailStatus(Enum):
    unRead = 0
    readed = 1
    selected = 2


class WarmUpScreenView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WarmUpScreenView, self).__init__()
        self.setupUi(self)

    def load_test_data(self):
        slm = QtCore.QStringListModel()
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        slm.setStringList(self.qList)
        self.statusView.setModel(slm)


if __name__ == "__main__":
    from assets import utils

    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = WarmUpScreenView()
    screen.load_test_data()
    screen.show()
    app.exec_()
