from enum import Enum
from PyQt5 import QtWidgets
from views.generated.new_warmup_module import Ui_MainWindow
from views.circular_widget_interface import CircularWidget

class WarmUpScreenView(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(WarmUpScreenView, self).__init__()
        self.setupUi(self)
        self.circular_widget = CircularWidget()
        self.circular_grid_layout.addWidget(self.circular_widget, 0,0,1,1)
        self.circular_widget.set_max_value(20)
        self.circular_widget.set_value(1)
        self.__sidebar_buttons = [self.main_btn, self.compose_btn, self.logs_btn]
        self.main_btn.clicked.connect(lambda: self.handle_sidebar_btn_clicked(0))
        self.compose_btn.clicked.connect(lambda: self.handle_sidebar_btn_clicked(1))
        self.logs_btn.clicked.connect(lambda: self.handle_sidebar_btn_clicked(2))

    def handle_sidebar_btn_clicked(self, target_index):
        for index, btn in enumerate(self.__sidebar_buttons):
            btn.setChecked(index == target_index)
        if self.stackedWidget.currentIndex() != target_index:
            if target_index == 0:
                self.select_frame.setVisible(True)
            else:
                self.select_frame.setVisible(False)
            self.stackedWidget.setCurrentIndex(target_index)
            self.pageSelectedSignal.emit(target_index)




if __name__ == "__main__":
    from assets import utils

    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = WarmUpScreenView()
    screen.show()
    app.exec_()
