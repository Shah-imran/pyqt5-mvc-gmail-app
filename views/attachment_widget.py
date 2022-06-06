from PyQt5 import QtWidgets, QtCore, QtGui

class AttachmentWidget(QtWidgets.QWidget):
    delSignal = QtCore.pyqtSignal(str)
    def __init__(self, icon, tip_text:str = "", file_path= ""):
        super(AttachmentWidget, self).__init__()
        self.target_file_path = file_path
        self.widget_layout = QtWidgets.QVBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 15, 12, 0)
        self.widget_layout.setSpacing(4)
        self.label_image = QtWidgets.QLabel()
        self.label_image = QtWidgets.QLabel()
        self.label_image.setToolTip("hello from the other world")
        self.label_image.setFixedSize(30, 40)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setPixmap(QtGui.QPixmap(icon))
        self.label_image.setScaledContents(True)
        self.widget_layout.addWidget(self.label_image)
        self.close_btn = QtWidgets.QPushButton()
        self.close_btn.setIconSize(QtCore.QSize(20, 20))
        self.close_btn.setIcon(QtGui.QIcon(":/icons/icons/close.png"))
        self.close_btn.setFixedSize(24, 24)
        self.close_btn.setFlat(True)
        self.widget_layout.addWidget(self.close_btn)
        v_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.label_image.setStyleSheet("background-color:transparent;")
        self.close_btn.setStyleSheet("""
        QPushButton{
             background-color:transparent;
             border-radius: 12px;
        }
        QPushButton:hover{
             border:1px solid #a6a6a6;
        }
        QToolTip { color:#000000; background-color:#FFFFFF; border: 0px; }"
        """)
        self.widget_layout.addItem(v_spacer)
        if len(tip_text) > 0:
            self.label_image.setToolTip(tip_text)
            self.close_btn.setToolTip(tip_text)
            self.label_image.setStyleSheet("""QToolTip { color:#000000; background-color:#FFFFFF; border: 0px; }""")

        self.close_btn.clicked.connect(lambda : self.delSignal.emit(file_path))
        self.adjustSize()

    def get_file_path(self):
        return self.target_file_path




