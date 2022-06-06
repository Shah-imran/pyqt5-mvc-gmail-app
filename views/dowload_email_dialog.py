from views.generated.generic_progress_dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import QtWidgets, QtGui


class ImapDownloadDialog(QtWidgets.QDialog, Ui_Dialog):
    dialog_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @pyqtSlot(float)
    def set_progressbar_value(self, value: float):
        self.progressBar.setValue(value)

    @pyqtSlot(str)
    def set_label_text(self, value: str):
        self.label_status.setText(value)

    @pyqtSlot(str)
    def change_button_text(self, value: str):
        self.pushButton_cancel.setText(value)

    @pyqtSlot()
    def close(self):
        self.accept()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        confirmation_window = QtWidgets.QMessageBox()
        result = confirmation_window.question(None, "Confirmation Window",
                                              "Are you sure?",
                                              confirmation_window.Ok | confirmation_window.Cancel)

        if result == confirmation_window.Ok:
            self.dialog_closed.emit()
        else:
            event.ignore()


