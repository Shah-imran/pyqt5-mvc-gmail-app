# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/inbox_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InboxTableWidget(object):
    def setupUi(self, InboxTableWidget):
        InboxTableWidget.setObjectName("InboxTableWidget")
        InboxTableWidget.resize(1366, 726)
        InboxTableWidget.setStyleSheet("#InboxTableWidget\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(239, 242, 248, 255), stop:1 rgba(188, 217, 235, 255));\n"
"}\n"
"QWidget\n"
"{\n"
"    background-color: transparent;\n"
"    color:black;\n"
"}\n"
"QTableWidget\n"
"{\n"
"    font-family: \"raleway\";\n"
"    font-size:18pt;\n"
"    outline: 0;\n"
"    border-width:1px;\n"
"    border-width:1px;\n"
"    border-style:solid;\n"
"    border-left-color: #a6a6a6;\n"
"    border-top-color: #a6a6a6;\n"
"    border-right-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    \n"
"}\n"
"QAbstractItemView::indicator { \n"
"    border:1px solid #a6a6a6;\n"
"    background-color: rgb(255, 255, 255);\n"
" }\n"
"QTableView::indicator:unchecked\n"
"{\n"
"     background-color: rgb(255, 255, 255);\n"
"}\n"
"QTableView::indicator:checked\n"
"{\n"
"     padding:2px;\n"
"     background-color: rgb(0, 0, 0);\n"
"}\n"
"QTableWidget:item:selected\n"
"{\n"
"  background-color: \"#DCE3ED\";\n"
"  color:black;\n"
"  border:none;\n"
"  outline: 0;\n"
"}\n"
"\n"
"QTextBrowser\n"
"{\n"
"    font: 12pt \"Raleway\";\n"
"   font-weight:300;\n"
"}\n"
"QTextEdit\n"
"{\n"
"     \n"
"    font: 12pt \"Raleway\";\n"
"   font-weight:300;\n"
"}\n"
"QScrollBar::vertical\n"
"{\n"
"  background-color: transparent;\n"
"  border: none;\n"
"  width:16px;\n"
"   padding-top:15px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"  background-color: gray;\n"
"  border-radius: 3px;\n"
"  min-width: 12px;\n"
"  min-height: 16px;\n"
"  margin:5px;\n"
"}\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"  height:0px;\n"
"  subcontrol-position: bottom;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"  height: 0px;\n"
"  subcontrol-position: top;\n"
"}\n"
"QScrollBar::horizontal\n"
"{\n"
"  background-color: transparent;\n"
"  border: none;\n"
"  height:20px;\n"
"}\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"  background-color: gray;\n"
"  border-radius: 5px;\n"
"  min-width: 16px;\n"
"  min-height: 16px;\n"
"  margin:5px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"height: 0px;\n"
"}\n"
"QAbstractScrollArea::corner {\n"
"    background: transparent;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(InboxTableWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.top_right_frame = QtWidgets.QFrame(InboxTableWidget)
        self.top_right_frame.setMinimumSize(QtCore.QSize(0, 75))
        self.top_right_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.top_right_frame.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.top_right_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_right_frame.setObjectName("top_right_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.top_right_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.gridLayout.addWidget(self.top_right_frame, 0, 1, 4, 1)
        self.top_left_frame = QtWidgets.QFrame(InboxTableWidget)
        self.top_left_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.top_left_frame.setStyleSheet("#first_fixed_lbl,  #a_z_radio,#latest_radio_opt\n"
"{\n"
"        font: 18pt \"Raleway\";\n"
"       font-weight:300;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"QDateEdit\n"
"{\n"
"    font: 16pt \"Montserrat\";\n"
"    background-color: #EFF2F8;\n"
"}\n"
"QDateEdit::drop-down \n"
"{\n"
"    border:none;\n"
"    background-color: #EFF2F8;\n"
"}\n"
"\n"
"\n"
"")
        self.top_left_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_left_frame.setObjectName("top_left_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_left_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateEdit_imap = QtWidgets.QDateEdit(self.top_left_frame)
        self.dateEdit_imap.setMinimumSize(QtCore.QSize(170, 30))
        self.dateEdit_imap.setMaximumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_imap.setFont(font)
        self.dateEdit_imap.setMouseTracking(True)
        self.dateEdit_imap.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateEdit_imap.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit_imap.setStyleSheet("QCalendarWidget > QWidget\n"
"{\n"
"  background-color: #a6a6a6;\n"
"  border: none;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton\n"
"{\n"
"  border: transparent;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QTableView\n"
"{\n"
"  border: transparent;\n"
"  background-color: rgb(255,255,255);\n"
"  selection-background-color: #028fc3;\n"
"  selection-color: white;\n"
"}\n"
"")
        self.dateEdit_imap.setWrapping(True)
        self.dateEdit_imap.setFrame(False)
        self.dateEdit_imap.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_imap.setReadOnly(False)
        self.dateEdit_imap.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_imap.setSpecialValueText("")
        self.dateEdit_imap.setAccelerated(False)
        self.dateEdit_imap.setKeyboardTracking(True)
        self.dateEdit_imap.setProperty("showGroupSeparator", True)
        self.dateEdit_imap.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_imap.setCalendarPopup(True)
        self.dateEdit_imap.setObjectName("dateEdit_imap")
        self.verticalLayout.addWidget(self.dateEdit_imap)
        self.ab_frame = QtWidgets.QFrame(self.top_left_frame)
        self.ab_frame.setMinimumSize(QtCore.QSize(150, 36))
        self.ab_frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ab_frame.setStyleSheet("")
        self.ab_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ab_frame.setObjectName("ab_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ab_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.a_radio_opt = QtWidgets.QRadioButton(self.ab_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_radio_opt.sizePolicy().hasHeightForWidth())
        self.a_radio_opt.setSizePolicy(sizePolicy)
        self.a_radio_opt.setStyleSheet("")
        self.a_radio_opt.setChecked(True)
        self.a_radio_opt.setObjectName("a_radio_opt")
        self.horizontalLayout.addWidget(self.a_radio_opt)
        self.label = QtWidgets.QLabel(self.ab_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 26pt \"Montserrat\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.b_radio_opt = QtWidgets.QRadioButton(self.ab_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_radio_opt.sizePolicy().hasHeightForWidth())
        self.b_radio_opt.setSizePolicy(sizePolicy)
        self.b_radio_opt.setStyleSheet("")
        self.b_radio_opt.setObjectName("b_radio_opt")
        self.horizontalLayout.addWidget(self.b_radio_opt)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.ab_frame)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_download = QtWidgets.QPushButton(self.top_left_frame)
        self.pushButton_download.setMinimumSize(QtCore.QSize(190, 30))
        self.pushButton_download.setMaximumSize(QtCore.QSize(190, 30))
        self.pushButton_download.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #028fc3;\n"
"       color:white;\n"
"       border:none; \n"
"    border-radius:5px;\n"
"    font: 13pt \"Raleway\";\n"
"    font-weight:500;\n"
"    margin-left: auto;\n"
"      margin-right: auto;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:15px;\n"
"       background-color: #108AB7;\n"
"    font: 12pt \"Raleway\";\n"
"}")
        self.pushButton_download.setObjectName("pushButton_download")
        self.verticalLayout_12.addWidget(self.pushButton_download)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.a_z_radio = QtWidgets.QRadioButton(self.top_left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_z_radio.sizePolicy().hasHeightForWidth())
        self.a_z_radio.setSizePolicy(sizePolicy)
        self.a_z_radio.setMinimumSize(QtCore.QSize(190, 0))
        self.a_z_radio.setMaximumSize(QtCore.QSize(190, 16777215))
        self.a_z_radio.setStyleSheet("QRadioButton\n"
"{\n"
"    font: 16pt \"Montserrat\";\n"
"    margin-left: 60px;\n"
"    margin-right: auto;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}")
        self.a_z_radio.setObjectName("a_z_radio")
        self.verticalLayout_12.addWidget(self.a_z_radio, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(67, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.latest_radio_opt = QtWidgets.QRadioButton(self.top_left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latest_radio_opt.sizePolicy().hasHeightForWidth())
        self.latest_radio_opt.setSizePolicy(sizePolicy)
        self.latest_radio_opt.setMinimumSize(QtCore.QSize(110, 0))
        self.latest_radio_opt.setMaximumSize(QtCore.QSize(105, 16777215))
        self.latest_radio_opt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.latest_radio_opt.setStyleSheet("")
        self.latest_radio_opt.setChecked(True)
        self.latest_radio_opt.setObjectName("latest_radio_opt")
        self.verticalLayout_2.addWidget(self.latest_radio_opt)
        self.first_fixed_lbl = QtWidgets.QLabel(self.top_left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_fixed_lbl.sizePolicy().hasHeightForWidth())
        self.first_fixed_lbl.setSizePolicy(sizePolicy)
        self.first_fixed_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.first_fixed_lbl.setObjectName("first_fixed_lbl")
        self.verticalLayout_2.addWidget(self.first_fixed_lbl, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.top_left_frame, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(InboxTableWidget)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(5)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(5)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 2, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(InboxTableWidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"   border:none;\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.firstPage = QtWidgets.QWidget()
        self.firstPage.setStyleSheet("")
        self.firstPage.setObjectName("firstPage")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.firstPage)
        self.verticalLayout_13.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mid_frame = QtWidgets.QFrame(self.firstPage)
        self.mid_frame.setMinimumSize(QtCore.QSize(800, 0))
        self.mid_frame.setStyleSheet("#mid_frame\n"
"{\n"
"     border-width:1px;\n"
"     border-style:solid;\n"
"     border-left-color: transparent;\n"
"     border-top-color: #a6a6a6;\n"
"     border-right-color: transparent;\n"
"     border-bottom-color:#a6a6a6;\n"
"}")
        self.mid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame.setObjectName("mid_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mid_frame)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.email_view_header_frame = QtWidgets.QFrame(self.mid_frame)
        self.email_view_header_frame.setStyleSheet("border:none;")
        self.email_view_header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.email_view_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email_view_header_frame.setObjectName("email_view_header_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.email_view_header_frame)
        self.horizontalLayout_5.setContentsMargins(27, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.email_view_header_frame)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font: 10pt \"Raleway\";\n"
"    font-weight:bold;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.from_email_lbl = QtWidgets.QLabel(self.email_view_header_frame)
        self.from_email_lbl.setStyleSheet("font: 10pt \"Raleway\";")
        self.from_email_lbl.setObjectName("from_email_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.from_email_lbl)
        self.label_3 = QtWidgets.QLabel(self.email_view_header_frame)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    font: 10pt \"Raleway\";\n"
"    font-weight:bold;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.to_email_lbl = QtWidgets.QLabel(self.email_view_header_frame)
        self.to_email_lbl.setStyleSheet("font: 10pt \"Raleway\";")
        self.to_email_lbl.setObjectName("to_email_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.to_email_lbl)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.email_topic_lbl = QtWidgets.QLabel(self.email_view_header_frame)
        self.email_topic_lbl.setStyleSheet("font: 16pt \"Raleway\";\n"
"font-weight:medium;")
        self.email_topic_lbl.setObjectName("email_topic_lbl")
        self.verticalLayout_4.addWidget(self.email_topic_lbl)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 4)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_3.addWidget(self.email_view_header_frame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.mid_frame)
        self.frame_3.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.inc_font_btn = QtWidgets.QPushButton(self.frame_3)
        self.inc_font_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.inc_font_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.inc_font_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/+_sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inc_font_btn.setIcon(icon)
        self.inc_font_btn.setIconSize(QtCore.QSize(38, 38))
        self.inc_font_btn.setAutoRepeat(True)
        self.inc_font_btn.setFlat(True)
        self.inc_font_btn.setObjectName("inc_font_btn")
        self.verticalLayout_7.addWidget(self.inc_font_btn)
        self.dec_font_btn = QtWidgets.QPushButton(self.frame_3)
        self.dec_font_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/-_sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dec_font_btn.setIcon(icon1)
        self.dec_font_btn.setIconSize(QtCore.QSize(38, 38))
        self.dec_font_btn.setFlat(True)
        self.dec_font_btn.setObjectName("dec_font_btn")
        self.verticalLayout_7.addWidget(self.dec_font_btn)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(20, 173, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.scrollArea = QtWidgets.QScrollArea(self.mid_frame)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 628, 280))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_layout.setObjectName("scroll_area_layout")
        self.textBrowser_email_body = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_email_body.setStyleSheet("")
        self.textBrowser_email_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_email_body.setObjectName("textBrowser_email_body")
        self.scroll_area_layout.addWidget(self.textBrowser_email_body)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addWidget(self.mid_frame)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        self.bottom_right_frame = QtWidgets.QFrame(self.firstPage)
        self.bottom_right_frame.setStyleSheet("")
        self.bottom_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_right_frame.setObjectName("bottom_right_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bottom_right_frame)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 20)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.attach_lbl_link = QtWidgets.QLabel(self.bottom_right_frame)
        self.attach_lbl_link.setMinimumSize(QtCore.QSize(34, 39))
        self.attach_lbl_link.setMaximumSize(QtCore.QSize(34, 39))
        self.attach_lbl_link.setText("")
        self.attach_lbl_link.setPixmap(QtGui.QPixmap(":/icons/icons/paperclip.svg.png"))
        self.attach_lbl_link.setAlignment(QtCore.Qt.AlignCenter)
        self.attach_lbl_link.setObjectName("attach_lbl_link")
        self.verticalLayout_6.addWidget(self.attach_lbl_link)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.bottom_right_frame)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 117, 123))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.attachment_h_layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.attachment_h_layout.setContentsMargins(0, 0, 0, 0)
        self.attachment_h_layout.setSpacing(0)
        self.attachment_h_layout.setObjectName("attachment_h_layout")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.attachment_h_layout.addItem(spacerItem13)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea_2)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.msg_to_send_editor = QtWidgets.QTextEdit(self.bottom_right_frame)
        self.msg_to_send_editor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.msg_to_send_editor.setObjectName("msg_to_send_editor")
        self.horizontalLayout_6.addWidget(self.msg_to_send_editor)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.forward_lbl_link = QtWidgets.QLabel(self.bottom_right_frame)
        self.forward_lbl_link.setMinimumSize(QtCore.QSize(38, 38))
        self.forward_lbl_link.setMaximumSize(QtCore.QSize(38, 38))
        self.forward_lbl_link.setText("")
        self.forward_lbl_link.setPixmap(QtGui.QPixmap(":/icons/icons/tl-redo.svg.png"))
        self.forward_lbl_link.setAlignment(QtCore.Qt.AlignCenter)
        self.forward_lbl_link.setObjectName("forward_lbl_link")
        self.verticalLayout_5.addWidget(self.forward_lbl_link)
        spacerItem14 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        self.send_btn = QtWidgets.QPushButton(self.bottom_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy)
        self.send_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.send_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.send_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #028fc3;\n"
"   color:white;\n"
"   border:none; \n"
"    border-radius:10px;\n"
"    font: 13pt \"Raleway\";\n"
"    font-weight:500;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:15px;\n"
"   background-color: #108AB7;\n"
"    font: 12pt \"Raleway\";\n"
"}")
        self.send_btn.setObjectName("send_btn")
        self.verticalLayout_5.addWidget(self.send_btn)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_13.addWidget(self.bottom_right_frame)
        self.verticalLayout_13.setStretch(0, 5)
        self.verticalLayout_13.setStretch(1, 2)
        self.stackedWidget.addWidget(self.firstPage)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.line_frame_2 = QtWidgets.QFrame(self.frame_2)
        self.line_frame_2.setStyleSheet("QFrame\n"
"{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-left-color: transparent;\n"
"border-top-color: #a6a6a6;\n"
"border-right-color: transparent;\n"
"border-bottom-color: transparent;\n"
"margin-right:40px;\n"
"}")
        self.line_frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_frame_2.setLineWidth(1)
        self.line_frame_2.setObjectName("line_frame_2")
        self.verticalLayout_10.addWidget(self.line_frame_2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 156, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem15)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setStyleSheet("font: 38pt \"Raleway\";\n"
"font-weight:light;\n"
"color: rgb(211, 215, 207);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(100, 100))
        self.label_4.setMaximumSize(QtCore.QSize(100, 100))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icons/mail icon_1.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        spacerItem18 = QtWidgets.QSpacerItem(20, 155, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem18)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)

        self.retranslateUi(InboxTableWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InboxTableWidget)

    def retranslateUi(self, InboxTableWidget):
        _translate = QtCore.QCoreApplication.translate
        InboxTableWidget.setWindowTitle(_translate("InboxTableWidget", "Form"))
        self.dateEdit_imap.setDisplayFormat(_translate("InboxTableWidget", "dd MM yyyy"))
        self.a_radio_opt.setText(_translate("InboxTableWidget", "A "))
        self.label.setText(_translate("InboxTableWidget", "/"))
        self.b_radio_opt.setText(_translate("InboxTableWidget", "B"))
        self.pushButton_download.setText(_translate("InboxTableWidget", "Download"))
        self.a_z_radio.setText(_translate("InboxTableWidget", "A - Z"))
        self.latest_radio_opt.setText(_translate("InboxTableWidget", "Earliest"))
        self.first_fixed_lbl.setText(_translate("InboxTableWidget", "First"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InboxTableWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InboxTableWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("InboxTableWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("InboxTableWidget", "New Column"))
        self.label_2.setText(_translate("InboxTableWidget", "From:"))
        self.from_email_lbl.setText(_translate("InboxTableWidget", "Mohamed Yehia -thedesrtm@gmail.com"))
        self.label_3.setText(_translate("InboxTableWidget", "To:"))
        self.to_email_lbl.setText(_translate("InboxTableWidget", "Mohamed Yehia -thedesrtm@gmail.com"))
        self.email_topic_lbl.setText(_translate("InboxTableWidget", "Friendly Outreach"))
        self.textBrowser_email_body.setHtml(_translate("InboxTableWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Raleway\'; font-size:12pt; font-weight:296; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-weight:24; color:#000000; background-color:#ffffff;\">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of &quot;de Finibus Bonorum et Malorum&quot; (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, &quot;Lorem ipsum dolor sit amet..&quot;, comes from a line in section 1.10.32.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-weight:24; color:#000000; background-color:#ffffff;\">The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from &quot;de Finibus Bonorum et Malorum&quot; by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.</span></p></body></html>"))
        self.msg_to_send_editor.setHtml(_translate("InboxTableWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Raleway\'; font-size:12pt; font-weight:296; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-weight:24; color:#000000; background-color:#ffffff;\">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of &quot;de Finibus Bonorum et Malorum&quot; (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, &quot;Lorem ipsum dolor sit amet..&quot;, comes from a line in section 1.10.32.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-weight:24; color:#000000; background-color:#ffffff;\">The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from &quot;de Finibus Bonorum et Malorum&quot; by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.</span></p></body></html>"))
        self.send_btn.setText(_translate("InboxTableWidget", "Send"))
        self.label_5.setText(_translate("InboxTableWidget", "MAILBOX EMPTY"))
import app_resources_rc
