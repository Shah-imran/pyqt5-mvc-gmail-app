from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from views.generated.configurations_screen import Ui_ConfigurationsScreen


class ConfigurationScreenView(QtWidgets.QWidget, Ui_ConfigurationsScreen):
    def __init__(self):
        super(ConfigurationScreenView, self).__init__()
        self.setupUi(self)

    @pyqtSlot(str)
    def set_analytics_account(self, value):
        self.analytics_account_lin.setText(value)

    @pyqtSlot(str)
    def set_campaign_name(self, value):
        self.campaign_name_lin.setText(value)

    @pyqtSlot(str)
    def set_webhook_url(self, value):
        self.webhook_url_lin.setText(value)

    @pyqtSlot(str)
    def set_target_blacklist(self, value):
        self.lineEdit_target_blacklist.setText(value)
