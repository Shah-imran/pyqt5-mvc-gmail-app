from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from models.main_model import MainModel
from config import UserConfig, ConfigManager


class ConfigurationController(QObject):
    # analytics_account_changed = pyqtSignal(str)
    # campaign_name_changed = pyqtSignal(str)
    # webhook_url_changed = pyqtSignal(str)
    # target_blacklist_changed = pyqtSignal(str)

    def __init__(self, model: MainModel):
        super().__init__()

        self._model = model

    def set_initial_value(self):
        self.update_analytics_account(UserConfig.tracking['analytics_account'])
        self.update_campaign_name(UserConfig.tracking['campaign_name'])
        self.update_webhook_url(UserConfig.webhook_link)
        self.update_target_blacklist(",".join(UserConfig.target_blacklist))

    @pyqtSlot(str)
    def update_analytics_account(self, value):
        self._model.configuration_model.analytics_account = value

    @pyqtSlot(str)
    def update_campaign_name(self, value):
        self._model.configuration_model.campaign_name = value

    @pyqtSlot(str)
    def update_webhook_url(self, value):
        self._model.configuration_model.webhook_url = value

    @pyqtSlot(str)
    def update_target_blacklist(self, value):
        self._model.configuration_model.target_blacklist = value

    @pyqtSlot()
    def save_config(self):
        self.config_manager = ConfigManager('save')
        self.config_manager.finished.connect(self.show_saving_finished_message)
        self.config_manager.finished.connect(self.config_manager.quit)
        self.config_manager.finished.connect(self.config_manager.deleteLater)
        self.config_manager.start()

    @pyqtSlot()
    def show_saving_finished_message(self):
        msg_box = QMessageBox()
        msg_box.setText('Config Saved')
        msg_box.exec_()


