from enum import Enum
from PyQt5 import QtWidgets, QtGui
from views.generated.compaign_screen import Ui_CampaignScreen
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class CampaignScreenView(QtWidgets.QWidget, Ui_CampaignScreen):
    def __init__(self):
        super(CampaignScreenView, self).__init__()
        self.setupUi(self)
        self._ab_radio_bold_font = QtGui.QFont("Montserrat", 34, QtGui.QFont.DemiBold)
        self._ab_radio_normal_font = QtGui.QFont("Montserrat", 34, QtGui.QFont.Light)
        self._radio_bold_font = QtGui.QFont("Montserrat", 24, QtGui.QFont.DemiBold)
        self._radio_normal_font = QtGui.QFont("Montserrat", 24, QtGui.QFont.Light)
        self._combo_normal_font = QtGui.QFont("Montserrat", 18, QtGui.QFont.Light)
        self._combo_bold_font = QtGui.QFont("Montserrat", 18, QtGui.QFont.DemiBold)
        self.a_radio_opt.setFont(self._ab_radio_bold_font)
        self.a_radio_opt.setChecked(True)
        self.b_radio_opt.setFont(self._ab_radio_normal_font)

        self.plain_opt.setFont(self._radio_bold_font)
        self.plain_opt.setChecked(True)
        self.html_opt.setFont(self._radio_normal_font)
        self.a_radio_opt.toggled.connect(self.handle_ab_option_changed)
        self.plain_opt.toggled.connect(self.handle_plain_option_changed)
        self._combo_buttons = [self.custom_host_name_check, self.email_tracking_check, self.webhoo_check,
                               self.remove_targets_check, self.check_for_blocks_opt]
        for box in self._combo_buttons:
            box.setFont(self._combo_normal_font)
            box.toggled.connect(lambda checked, b=box: self.get_check_lambda_factory(checked, b))

    @pyqtSlot(int)
    def number_of_accounts_update(self, value: int):
        self.number_of_accounts_spin.setValue(value)

    @pyqtSlot(int)
    def emails_per_account_update(self, value: int):
        self.emails_per_account_spin.setValue(value)

    @pyqtSlot(int)
    def delay_from(self, value: int):
        self.delay_from.setText(str(value))

    @pyqtSlot(int)
    def delay_to(self, value: int):
        self.delay_to.setText(str(value))

    @pyqtSlot(bool)
    def compose_plain_radio(self, value: bool):
        self.plain_opt.setChecked(value)

    @pyqtSlot(bool)
    def compose_html_radio(self, value: bool):
        self.html_opt.setChecked(value)

    def get_check_lambda_factory(self, checked, box):
        box.setFont(
            self._combo_bold_font if checked else self._combo_normal_font
        )
        
    def handle_ab_option_changed(self):
        if self.a_radio_opt.isChecked():
            self.a_radio_opt.setFont(self._ab_radio_bold_font)
            self.b_radio_opt.setFont(self._ab_radio_normal_font)
        else:
            self.a_radio_opt.setFont(self._ab_radio_normal_font)
            self.b_radio_opt.setFont(self._ab_radio_bold_font)

    def handle_plain_option_changed(self):
        if self.plain_opt.isChecked():
            self.plain_opt.setFont(self._radio_bold_font)
            self.html_opt.setFont(self._radio_normal_font)
        else:
            self.plain_opt.setFont(self._radio_normal_font)
            self.html_opt.setFont(self._radio_bold_font)


if __name__ == "__main__":
    from assets import utils
    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    screen = CampaignScreenView()
    screen.showMaximized()
    app.exec_()
