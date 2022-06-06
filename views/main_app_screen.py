from enum import Enum
from PyQt5 import QtWidgets, QtGui, QtCore
from views.generated.main_app_window import Ui_MainWindow
from views.inbox_screen import InboxScreenView, EmailStatus
from views.compaign_screen import CampaignScreenView
from views.database_screen import DatabaseScreenView
from views.configurations_screen import ConfigurationScreenView
from views.attachment_widget import AttachmentWidget
from assets import utils


class MainAppWindow(QtWidgets.QWidget, Ui_MainWindow):
    pageSelectedSignal = QtCore.pyqtSignal(int)  # page index

    def __init__(self):
        super(MainAppWindow, self).__init__()
        self.setupUi(self)
        # create pages
        self.inbox_screen = InboxScreenView()
        self.campaign_screen = CampaignScreenView()
        self.db_screen = DatabaseScreenView()
        self.configuration_window = ConfigurationScreenView()

        # add pages
        self.stackedWidget.addWidget(self.inbox_screen)
        self.stackedWidget.addWidget(self.campaign_screen)
        self.stackedWidget.addWidget(self.db_screen)
        self.stackedWidget.addWidget(self.configuration_window)
        self.setStyleSheet(utils.load_app_style())
        self.setWindowTitle("GMonster")

        # signals
        self.inbox_btn.clicked.connect(
            lambda: self.handle_sidebar_btn_clicked(0))
        self.compaign_btn.clicked.connect(
            lambda: self.handle_sidebar_btn_clicked(1))
        self.database_btn.clicked.connect(
            lambda: self.handle_sidebar_btn_clicked(2))
        self.configurations_btn.clicked.connect(
            lambda: self.handle_sidebar_btn_clicked(3))
        self.__sidebar_buttons = [
            self.inbox_btn, self.compaign_btn, self.database_btn, self.configurations_btn]

    def test_add_fake_data(self):
        self.inbox_screen.tableWidget.setRowCount(0)
        row_index = self.inbox_screen.tableWidget.rowCount()
        self.inbox_screen.tableWidget.insertRow(row_index)
        self.inbox_screen.add_row(
            row_index, "mohamed ", "check your email", "19-5", EmailStatus.selected)
        row_index = self.inbox_screen.tableWidget.rowCount()
        self.inbox_screen.tableWidget.insertRow(row_index)
        self.inbox_screen.add_row(
            row_index, "mohamed ", "check your email", "19-5", EmailStatus.unRead)
        row_index = self.inbox_screen.tableWidget.rowCount()
        self.inbox_screen.tableWidget.insertRow(row_index)
        self.inbox_screen.add_row(
            row_index, "mohamed ", "check your email", "19-5", EmailStatus.readed)
        self.attachment1 = AttachmentWidget(
            ":/icons/icons/file-image 2.svg.png", "file1.txt")
        self.attachment2 = AttachmentWidget(
            ":/icons/icons/file-image 2.svg.png")
        self.inbox_screen.attachment_h_layout.insertWidget(0, self.attachment1)
        self.inbox_screen.attachment_h_layout.insertWidget(1, self.attachment2)
        self.attachment3 = AttachmentWidget(
            ":/icons/icons/file-image 2.svg.png")
        self.attachment4 = AttachmentWidget(
            ":/icons/icons/file-image 2.svg.png")
        self.attachment5 = AttachmentWidget(
            ":/icons/icons/file-image 2.svg.png")
        self.attachment6 = AttachmentWidget(
            ":/icons/icons/file-image 2.svg.png")
        self.campaign_screen.attachment_layout.insertWidget(
            0, self.attachment3)
        self.campaign_screen.attachment_layout.insertWidget(
            0, self.attachment4)
        self.campaign_screen.attachment_layout.insertWidget(
            0, self.attachment5)
        self.campaign_screen.attachment_layout.insertWidget(
            0, self.attachment6)


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

    def set_new_emails_count(self, new_emails: int):
        self.new_emails_count_lbl.setText(f"{new_emails}")


if __name__ == "__main__":
    from assets import utils
    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = MainAppWindow()
    screen.test_add_fake_data()
    screen.showMaximized()
    app.exec_()
