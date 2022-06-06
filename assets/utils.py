import os
from PyQt5 import QtCore, QtGui
import app_resources_rc
rp = os.path.dirname(os.path.realpath(__file__))
APP_THEME = os.path.join(rp, "..", "assets", "app_style.css")


def load_app_fonts():
    # montserrat
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/Montserrat-Bold.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/MontserratAlternates-Medium.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/MontserratAlternates-Regular.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/MontserratAlternates-Light.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/Montserrat-Medium.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/Montserrat-Light.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/Montserrat-Regular.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/MontserratAlternates-SemiBold.otf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/montserrat/Montserrat-Thin.otf")
    # raleway
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-ThinItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-SemiBold.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-LightItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Thin.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Bold.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-SemiBoldItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-BlackItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Medium.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-ExtraBold.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Black.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-BoldItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-ExtraBoldItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-ExtraLight.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Light.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-ExtraLightItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-MediumItalic.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/raleway/Raleway-Italic.ttf")


def load_app_style():
    with open(APP_THEME) as css_file:
        return css_file.read()