from PyQt5 import QtWidgets, QtCore, QtGui


class FramelessScreen(QtWidgets.QDialog):
    def __init__(self):
        super(FramelessScreen, self).__init__()
        self.widget_layout = QtWidgets.QVBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(0)
        self.header_frame = QtWidgets.QFrame()
        self.header_frame.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.header_frame.setObjectName("frameless_screen_header_frame")
        self.header_layout = QtWidgets.QHBoxLayout(self.header_frame)
        self.header_layout.setContentsMargins(0,0,0,0)
        self.logo_image = QtWidgets.QLabel()
        self.logo_image.setFixedSize(34, 25)
        self.logo_image.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_image.setPixmap(QtGui.QPixmap(":/icons/icons/monster-oldalra.png"))
        self.logo_image.setScaledContents(True)
        self.header_layout.addWidget(self.logo_image)
        h_spacer_1 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.header_layout.addItem(h_spacer_1)
        self.close_btn = QtWidgets.QPushButton()
        self.close_btn.setFixedSize(36, 30)
        self.close_btn.setIconSize(QtCore.QSize(35, 30))
        self.close_btn.setIcon(QtGui.QIcon(":/icons/icons/close.png"))
        self.close_btn.setObjectName("frameless_screen_close_btn")
        self.close_btn.setFlat(True)
        self.hide_btn = QtWidgets.QPushButton()
        self.hide_btn.setFixedSize(36, 30)
        self.hide_btn.setIconSize(QtCore.QSize(35, 30))
        self.hide_btn.setIcon(QtGui.QIcon(":/icons/icons/hide.png"))
        self.hide_btn.setObjectName("frameless_screen_hide_btn")
        self.hide_btn.setFlat(True)
        self.header_layout.addWidget(self.hide_btn)
        self.header_layout.addWidget(self.close_btn)
        self.widget_layout.addWidget(self.header_frame, stretch=0)
        # main content frame
        self.content_frame = QtWidgets.QFrame()
        self.content_frame.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.content_frame.setObjectName("frameless_screen_content_frame")
        self.widget_layout.addWidget(self.content_frame, stretch=1)

        self.cur_y = 0
        self.cur_x = 0
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        app_screen = QtWidgets.QApplication.desktop().screen().rect().center()
        self.move(app_screen - self.frameGeometry().center())
        self.close_btn.clicked.connect(lambda: self.close())
        self.hide_btn.clicked.connect(lambda: self.showMinimized())

    def set_central_widget(self, ref_widget):
        self.frame_layout = QtWidgets.QGridLayout(self.content_frame)
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.content_frame.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.frame_layout.addWidget(ref_widget, 0,0,1,1, alignment=QtCore.Qt.AlignCenter)


    def mousePressEvent(self, event):
        self.cur_x = event.x()
        self.cur_y = event.y()

    def mouseMoveEvent(self, event):
        self.move(event.globalX() - self.cur_x, event.globalY() - self.cur_y)
