# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_app_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 530)
        MainWindow.setStyleSheet("#frameless_screen_header_frame\n"
"{\n"
"    background-color:white;\n"
"}\n"
"#frameless_screen_content_frame\n"
"{\n"
"    background-color:#eff2f8;\n"
"}\n"
"#frameless_screen_hide_btn , #frameless_screen_close_btn\n"
"{\n"
"    border:none;\n"
"}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sidebar_frame = QtWidgets.QFrame(MainWindow)
        self.sidebar_frame.setStyleSheet("#sidebar_frame\n"
"{\n"
"        background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(239, 242, 248, 255), stop:1 rgba(188, 217, 235, 255));\n"
"}\n"
"QProgressBar\n"
"{\n"
"  background-color: white;\n"
"  border:none;\n"
"  border-radius:5px;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"  background-color: #2275FB;\n"
"  border-radius:5px;\n"
"}\n"
"QWidget\n"
"{\n"
"    font: 14pt \"Raleway\";\n"
"    font-weight:300;\n"
"\n"
"}\n"
"QPushButton\n"
"{\n"
"   text-align: left;\n"
"   padding-left:10px;\n"
"   \n"
"}\n"
"QPushButton:checked\n"
"{\n"
"   border:none;\n"
"   font-weight:bold;\n"
"}\n"
"#new_emails_count_lbl\n"
"{\n"
"   padding-right:10px;\n"
"    color: #028fc3;\n"
"    font-weight:bold;\n"
"}\n"
"")
        self.sidebar_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sidebar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_frame.setObjectName("sidebar_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(self.sidebar_frame)
        self.logo.setMinimumSize(QtCore.QSize(200, 100))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.logo.setStyleSheet("padding-left:0px;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/icons/icons/main_logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.line_frame = QtWidgets.QFrame(self.sidebar_frame)
        self.line_frame.setStyleSheet("QFrame\n"
"{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-left-color: transparent;\n"
"border-top-color: #a6a6a6;\n"
"border-right-color: transparent;\n"
"border-bottom-color: transparent;\n"
"}")
        self.line_frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_frame.setLineWidth(1)
        self.line_frame.setObjectName("line_frame")
        self.verticalLayout_2.addWidget(self.line_frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inbox_btn = QtWidgets.QPushButton(self.sidebar_frame)
        self.inbox_btn.setStyleSheet("")
        self.inbox_btn.setCheckable(True)
        self.inbox_btn.setChecked(True)
        self.inbox_btn.setFlat(True)
        self.inbox_btn.setObjectName("inbox_btn")
        self.horizontalLayout.addWidget(self.inbox_btn)
        self.new_emails_count_lbl = QtWidgets.QLabel(self.sidebar_frame)
        self.new_emails_count_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.new_emails_count_lbl.setObjectName("new_emails_count_lbl")
        self.horizontalLayout.addWidget(self.new_emails_count_lbl)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.compaign_btn = QtWidgets.QPushButton(self.sidebar_frame)
        self.compaign_btn.setStyleSheet("")
        self.compaign_btn.setCheckable(True)
        self.compaign_btn.setChecked(False)
        self.compaign_btn.setFlat(True)
        self.compaign_btn.setObjectName("compaign_btn")
        self.verticalLayout.addWidget(self.compaign_btn)
        self.database_btn = QtWidgets.QPushButton(self.sidebar_frame)
        self.database_btn.setStyleSheet("")
        self.database_btn.setCheckable(True)
        self.database_btn.setChecked(False)
        self.database_btn.setFlat(True)
        self.database_btn.setObjectName("database_btn")
        self.verticalLayout.addWidget(self.database_btn)
        self.configurations_btn = QtWidgets.QPushButton(self.sidebar_frame)
        self.configurations_btn.setStyleSheet("")
        self.configurations_btn.setCheckable(True)
        self.configurations_btn.setChecked(False)
        self.configurations_btn.setFlat(True)
        self.configurations_btn.setObjectName("configurations_btn")
        self.verticalLayout.addWidget(self.configurations_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.select_frame = QtWidgets.QFrame(self.sidebar_frame)
        self.select_frame.setStyleSheet("font:14pt \"Raleway\";\n"
"font-weight:300;")
        self.select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.select_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_frame.setObjectName("select_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.select_frame)
        self.horizontalLayout_2.setContentsMargins(24, -1, 24, 15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.trash_lbl = QtWidgets.QLabel(self.select_frame)
        self.trash_lbl.setMinimumSize(QtCore.QSize(22, 27))
        self.trash_lbl.setMaximumSize(QtCore.QSize(22, 27))
        self.trash_lbl.setText("")
        self.trash_lbl.setPixmap(QtGui.QPixmap(":/icons/icons/trash.svg.png"))
        self.trash_lbl.setScaledContents(True)
        self.trash_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.trash_lbl.setObjectName("trash_lbl")
        self.horizontalLayout_2.addWidget(self.trash_lbl)
        self.select_all_lbl = QtWidgets.QLabel(self.select_frame)
        self.select_all_lbl.setObjectName("select_all_lbl")
        self.horizontalLayout_2.addWidget(self.select_all_lbl)
        self.label = QtWidgets.QLabel(self.select_frame)
        self.label.setMinimumSize(QtCore.QSize(22, 22))
        self.label.setMaximumSize(QtCore.QSize(22, 22))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/forward selected.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.select_frame)
        self.sending_progress_frame = QtWidgets.QFrame(self.sidebar_frame)
        self.sending_progress_frame.setStyleSheet("font: 8pt \"Raleway\";\n"
"font-weight:300;")
        self.sending_progress_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sending_progress_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sending_progress_frame.setObjectName("sending_progress_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.sending_progress_frame)
        self.gridLayout.setContentsMargins(24, -1, 24, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.sending_progress_bar = QtWidgets.QProgressBar(self.sending_progress_frame)
        self.sending_progress_bar.setMinimumSize(QtCore.QSize(0, 10))
        self.sending_progress_bar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.sending_progress_bar.setProperty("value", 24)
        self.sending_progress_bar.setTextVisible(False)
        self.sending_progress_bar.setObjectName("sending_progress_bar")
        self.gridLayout.addWidget(self.sending_progress_bar, 0, 0, 1, 2)
        self.sending_status_lbl = QtWidgets.QLabel(self.sending_progress_frame)
        self.sending_status_lbl.setObjectName("sending_status_lbl")
        self.gridLayout.addWidget(self.sending_status_lbl, 1, 0, 1, 1)
        self.sending_progress_lbl = QtWidgets.QLabel(self.sending_progress_frame)
        self.sending_progress_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sending_progress_lbl.setObjectName("sending_progress_lbl")
        self.gridLayout.addWidget(self.sending_progress_lbl, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.sending_progress_frame)
        self.horizontalLayout_3.addWidget(self.sidebar_frame)
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(239, 242, 248, 255), stop:1 rgba(188, 217, 235, 255));\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.inbox_btn.setText(_translate("MainWindow", "Inbox"))
        self.new_emails_count_lbl.setText(_translate("MainWindow", "0"))
        self.compaign_btn.setText(_translate("MainWindow", "Campaign"))
        self.database_btn.setText(_translate("MainWindow", "Database"))
        self.configurations_btn.setText(_translate("MainWindow", "Configurations"))
        self.select_all_lbl.setText(_translate("MainWindow", "Select All"))
        self.sending_status_lbl.setText(_translate("MainWindow", "Sending"))
        self.sending_progress_lbl.setText(_translate("MainWindow", "13/200"))
import app_resources_rc
