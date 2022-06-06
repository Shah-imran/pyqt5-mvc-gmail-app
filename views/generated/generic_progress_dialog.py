# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/generic_progress_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 132)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_status = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_status.setFont(font)
        self.label_status.setText("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("QPushButton {\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #4B7DAD\n"
"        );\n"
"    padding: 5px 28px;\n"
"    color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #709fb0\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    }")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GMonster"))
        self.pushButton_cancel.setText(_translate("Dialog", "CANCEL"))
