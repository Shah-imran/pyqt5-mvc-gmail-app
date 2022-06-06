# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/first_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FirstScreen(object):
    def setupUi(self, FirstScreen):
        FirstScreen.setObjectName("FirstScreen")
        FirstScreen.resize(830, 324)
        FirstScreen.setMinimumSize(QtCore.QSize(600, 200))
        FirstScreen.setMaximumSize(QtCore.QSize(16777215, 16777215))
        FirstScreen.setWindowTitle("")
        FirstScreen.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FirstScreen)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.signup_btn = QtWidgets.QPushButton(FirstScreen)
        self.signup_btn.setMinimumSize(QtCore.QSize(180, 40))
        self.signup_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.signup_btn.setObjectName("signup_btn")
        self.horizontalLayout.addWidget(self.signup_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.login_btn = QtWidgets.QPushButton(FirstScreen)
        self.login_btn.setMinimumSize(QtCore.QSize(180, 40))
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_btn.setStyleSheet("")
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.updates_progress_bar = QtWidgets.QProgressBar(FirstScreen)
        self.updates_progress_bar.setMinimumSize(QtCore.QSize(300, 10))
        self.updates_progress_bar.setMaximumSize(QtCore.QSize(300, 10))
        self.updates_progress_bar.setStyleSheet("")
        self.updates_progress_bar.setProperty("value", 24)
        self.updates_progress_bar.setTextVisible(False)
        self.updates_progress_bar.setFormat("")
        self.updates_progress_bar.setObjectName("updates_progress_bar")
        self.verticalLayout.addWidget(self.updates_progress_bar)
        self.checking_updates_lbl = QtWidgets.QLabel(FirstScreen)
        self.checking_updates_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.checking_updates_lbl.setObjectName("checking_updates_lbl")
        self.verticalLayout.addWidget(self.checking_updates_lbl)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(FirstScreen)
        QtCore.QMetaObject.connectSlotsByName(FirstScreen)

    def retranslateUi(self, FirstScreen):
        _translate = QtCore.QCoreApplication.translate
        self.signup_btn.setText(_translate("FirstScreen", "Sign Up"))
        self.login_btn.setText(_translate("FirstScreen", "Log In"))
        self.checking_updates_lbl.setText(_translate("FirstScreen", "Checking for updates"))
import app_resources_rc