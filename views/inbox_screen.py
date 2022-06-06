from enum import Enum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from views.generated.inbox_screen import Ui_InboxTableWidget
from views.dowload_email_dialog import ImapDownloadDialog
import re
from config import logger
import traceback


def prepare_html(body):
    # print(body)
    mails = re.findall('[\w\.-]+@[\w\.-]+\.\w+', body)
    urls = re.findall('https?://[^\s<>"]+|www\.[^\s<>"]+', body)
    for item in urls:
        try:
            a_tag = '<a href="{}">{}</a>'.format(item, item)
            if "<{}>".format(item) in body:
                body = body.replace("<{}>".format(item), a_tag)
            else:
                body = body.replace(" {}".format(item), " " + a_tag)
                body = body.replace("\n{}".format(item), "\n" + a_tag)
        except:
            pass

    for item in mails:
        try:
            a_tag = ' <a href="mailto:{}">{}</a>'.format(item, item)
            body = body.replace(" {}".format(item), a_tag)

        except:
            pass
    body = body.replace("\n", '<br>')
    # print(body)
    html = """<!doctype html>

            <html lang="en">
            <head>
            <meta charset="utf-8">

            <title>The HTML5 Herald</title>
            <meta name="description" content="The HTML5 Herald">
            <meta name="author" content="SitePoint">


            </head>

            <body>
            <p>{}</p>

            </body>
            </html>""".format(body)

    return html


class EmailStatus(Enum):
    unRead = 0
    readed = 1
    selected = 2


class InboxScreenView(QtWidgets.QWidget, Ui_InboxTableWidget):
    email_marked = pyqtSignal(str, bool)
    open_email = pyqtSignal(str, int)

    def __init__(self):
        super(InboxScreenView, self).__init__()
        self.setupUi(self)
        self.a_radio_opt.setChecked(True)
        self.a_z_radio.setChecked(False)
        '''self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent, False)'''
        self._radio_bold_font = QtGui.QFont("Montserrat", 20, QtGui.QFont.DemiBold)
        self._radio_normal_font = QtGui.QFont("Montserrat", 20, QtGui.QFont.Light)
        self.a_radio_opt.setFont(self._radio_bold_font)
        self.b_radio_opt.setFont(self._radio_normal_font)
        self.a_radio_opt.toggled.connect(self.handle_ab_option_changed)
        self.a_z_radio.toggled.connect(self.handle_az_option_changed)
        self.latest_radio_opt.toggled.connect(self.handle_latest_option_changed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setColumnWidth(2, 5)
        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.clicked.connect(self.handle_row_selected)
        self.textBrowser_email_body.anchorClicked.connect(
            QtGui.QDesktopServices.openUrl
        )

        self.dialog = ImapDownloadDialog()

    @pyqtSlot(str)
    def set_to_email_lbl(self, value: str):
        self.to_email_lbl.setText(value)

    @pyqtSlot(str)
    def set_from_email_lbl(self, value: str):
        self.from_email_lbl.setText(value)

    @pyqtSlot(str)
    def set_email_topic_lbl(self, value: str):
        self.email_topic_lbl.setText(value)

    @pyqtSlot(int)
    def set_email_body_font_size(self, value: int):
        self.textBrowser_email_body.selectAll()
        self.textBrowser_email_body.setFontPointSize(value)

    @pyqtSlot(str)
    def set_email_body(self, value: str):
        try:
            if "</body>" in value:
                pass
            else:
                value = "FROM - {} <br>SUBJECT - {}<br><br>{}".format(
                    self.from_email_lbl.text(), self.email_topic_lbl.text(), value)

                value = prepare_html(value)

            self.textBrowser_email_body.clear()
            self.textBrowser_email_body.setText(value)
            self.textBrowser_email_body.setTextColor(QtCore.Qt.black)

        except Exception as e:
            logger.error(f"Error at views.inbox_screen.InboxScreenView: {e}\n{traceback.format_exc()}")

    @pyqtSlot(str)
    def set_date(self, value):
        date = QtCore.QDate.fromString(value, "M/d/yyyy")
        self.dateEdit_imap.setDate(date)

    def handle_ab_option_changed(self):
        if self.a_radio_opt.isChecked():
            self.a_radio_opt.setFont(self._radio_bold_font)
            self.b_radio_opt.setFont(self._radio_normal_font)
        else:
            self.a_radio_opt.setFont(self._radio_normal_font)
            self.b_radio_opt.setFont(self._radio_bold_font)

    def handle_az_option_changed(self):
        if self.a_z_radio.isChecked():
            self.a_z_radio.setText("Z - A")
        else:
            self.a_z_radio.setText("A - Z")

    def handle_latest_option_changed(self):
        if self.latest_radio_opt.isChecked():
            self.latest_radio_opt.setText("Earliest")
        else:
            self.latest_radio_opt.setText("Latest")

    def get_color(self, state: EmailStatus):
        color = QtGui.QColor("#DCE3ED")
        if state == EmailStatus.unRead:
            color = QtCore.Qt.white
        elif state == EmailStatus.readed:
            color = QtCore.Qt.transparent
        return color

    def add_row(self, index, name, subject, date_as_str, uid, email_status: EmailStatus):
        color = self.get_color(email_status)
        un_checked_item = QtWidgets.QTableWidgetItem()
        un_checked_item.setCheckState(QtCore.Qt.Unchecked)
        un_checked_item.setBackground(color)
        un_checked_item.setData(QtCore.Qt.DecorationRole, uid)
        self.tableWidget.setItem(index, 0, un_checked_item)

        self.tableWidget.setItem(index, 1, self.create_table_item(name, color, font_weight=QtGui.QFont.Medium,
                                                                  align=QtCore.Qt.AlignLeft))
        self.tableWidget.setItem(index, 2, self.create_table_item("|", color, align=QtCore.Qt.AlignCenter,
                                                                  font_color=QtCore.Qt.gray))
        self.tableWidget.setItem(index, 3, self.create_table_item(subject, color, font_weight=QtGui.QFont.Normal,
                                                                  align=QtCore.Qt.AlignLeft))
        self.tableWidget.setItem(index, 4,
                                 self.create_table_item(date_as_str, color, font_size=11, align=QtCore.Qt.AlignRight))

    def create_table_item(self, value, color, font_name="raleway", font_size=16, font_weight=QtGui.QFont.Normal,
                          align=QtCore.Qt.AlignCenter, font_color=QtCore.Qt.black):
        font = QtGui.QFont(font_name, font_size, font_weight)
        item = QtWidgets.QTableWidgetItem()
        item.setText(value)
        item.setTextAlignment(align)
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setForeground(QtGui.QBrush(font_color))
        item.setFont(font)
        item.setBackground(color)
        return item

    def change_row_color(self, row_index, color):
        print(row_index)
        for i in range(5):
            item = self.tableWidget.item(row_index, i)
            item.setBackground(color)

    def handle_row_selected(self, model_index):
        if model_index.column() != 0:
            color = self.get_color(EmailStatus.selected)
            self.change_row_color(model_index.row(), color)

            self.open_email.emit(
                self.tableWidget.item(model_index.row(), 0).data(QtCore.Qt.DecorationRole),
                model_index.row()
            )
        else:
            state: bool = True if self.tableWidget.item(model_index.row(), 0).checkState() else False
            uid: str = self.tableWidget.item(model_index.row(), 0).data(QtCore.Qt.DecorationRole)

            self.email_marked.emit(uid, state)


if __name__ == "__main__":
    from assets import utils

    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = InboxScreenView()
    screen.tableWidget.setRowCount(0)
    row_index = screen.tableWidget.rowCount()
    screen.tableWidget.insertRow(row_index)
    screen.add_row(row_index, "mohamed", "check your email", "19-5", EmailStatus.selected)
    screen.change_row_color(0, QtCore.Qt.green)
    screen.showMaximized()
    app.exec_()
