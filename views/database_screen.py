from enum import Enum
from PyQt5 import QtWidgets, QtGui, QtCore
from views.generated.database_screen import Ui_DatabaseScreen
from PyQt5.QtCore import pyqtSlot


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeft

    def headerData(self, section: int, orientation, role: int = ...):
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeading
        elif role == QtCore.Qt.FontRole:
            font = QtGui.QFont("Raleway", 22, QtGui.QFont.DemiBold)
            return font
        else:
            return super(TableModel, self).headerData(section, orientation, role)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class DatabaseScreenView(QtWidgets.QWidget, Ui_DatabaseScreen):
    radioButtonCheckedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(DatabaseScreenView, self).__init__()
        self.setupUi(self)
        self._option_bold_font = QtGui.QFont("Montserrat", 20, QtGui.QFont.DemiBold)
        self._option_normal_font = QtGui.QFont("Montserrat", 20, QtGui.QFont.Light)
        self._all_options = [self.groupa_radio, self.groupb_radio, self.target_radio]
        for box in self._all_options:
            box.setFont(self._option_normal_font)
            box.toggled.connect(lambda checked, b=box: self.get_check_lambda_factory(checked, b))
    @pyqtSlot(bool)
    def set_group_a_checkbox(self, value: bool):
        self.groupa_checkbox.setChecked(value)

    @pyqtSlot(bool)
    def set_group_b_checkbox(self, value: bool):
        self.groupb_checkbox.setChecked(value)

    @pyqtSlot(bool)
    def set_target_checkbox(self, value: bool):
        self.target_checkbox.setChecked(value)

    def generate_test_data(self):
        data = [
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8], [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],
            [4, 9, 2, 4, 9, 2, 4, 8, 4, 8],

        ]
        self.model = TableModel(data)
        self.tableView.setModel(self.model)

    def get_check_lambda_factory(self, checked, box, ):
        box.setFont(
            self._option_bold_font if checked else self._option_normal_font
        )
        self.radioButtonCheckedSignal.emit()


if __name__ == "__main__":
    from assets import utils

    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = DatabaseScreenView()
    screen.showMaximized()
    app.exec_()
