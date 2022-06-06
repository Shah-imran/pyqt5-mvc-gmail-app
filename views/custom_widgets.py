from PyQt5 import QtWidgets, QtCore, QtGui


class PasswordLine(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(PasswordLine, self).__init__(parent)
        self.button = QtWidgets.QPushButton(self)
        icon_file = ":/icons/icons/icons8-eye-30.png"
        self.button.setIcon(QtGui.QIcon(icon_file))
        self.button.setFixedSize(30, 30)
        self.button.setFlat(True)
        self.button.setStyleSheet("border:none;")
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.clicked.connect(self.invert_mode)
        frameWidth = self.style().pixelMetric(QtWidgets.QStyle.PM_DefaultFrameWidth)
        buttonSize = self.button.sizeHint()
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth*2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth*2 + 2))
        self.setCursor(QtCore.Qt.ArrowCursor)


    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(QtWidgets.QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right()+220 - frameWidth - buttonSize.width()-2,
                         (self.rect().bottom() - buttonSize.height() + 1)/2+10)
        super(PasswordLine, self).resizeEvent(event)

    def setEchoMode(self, mode):
        super(PasswordLine, self).setEchoMode(mode)
        if mode == QtWidgets.QLineEdit.Normal:
            icon = QtGui.QIcon(":/icons/icons/icons8-hide-50.png")
            self.button.setIcon(icon)
        elif mode == QtWidgets.QLineEdit.Password:
            icon = QtGui.QIcon(":/icons/icons/icons8-eye-30.png")
            self.button.setIcon(icon)

    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        return super(PasswordLine, self).focusOutEvent(a0)


    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        return  super(PasswordLine, self).focusInEvent(a0)

    def invert_mode(self):
        if self.echoMode() == QtWidgets.QLineEdit.Normal:
            self.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.setEchoMode(QtWidgets.QLineEdit.Normal)
