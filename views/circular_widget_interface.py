from PyQt5 import QtWidgets, QtCore
from views.generated.circular_widget_view import Ui_Form


class CircularWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(CircularWidget, self).__init__()
        self.setupUi(self)
        self.__max_value = 0
    
    def set_max_value(self, value:int):
        self.__max_value = value
    
    def set_value(self, value:int):
        self.phase_number_lbl.setText(str(value))
        maped_value = value*100/self.__max_value
        self._progressbar_value(maped_value)


    
    def _progressbar_value(self, value):
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
        styleSheet = """
            QFrame{
                border-radius: 110px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:%s rgba(255, 0, 127, 0), stop:%s rgba(34, 117, 251, 255));
            }
        """%(stop_1, stop_2)
        self.progress_frame.setStyleSheet(styleSheet)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    s = CircularWidget()
    s.set_max_value(7)
    s.set_value(5)
    s.show()
    app.exec_()