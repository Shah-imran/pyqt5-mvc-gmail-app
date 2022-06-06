from PyQt5.QtCore import QObject, pyqtSignal
import re
from config import AppConfig, UserConfig


class ConfigurationModel(QObject):
    analytics_account_changed = pyqtSignal(str)
    campaign_name_changed = pyqtSignal(str)
    webhook_url_changed = pyqtSignal(str)
    target_blacklist_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self._analytics_account = ''
        self._campaign_name = ''
        self._webhook_url = ''
        self._target_blacklist = ''

    @property
    def analytics_account(self):
        return self._analytics_account

    @analytics_account.setter
    def analytics_account(self, value):
        UserConfig.tracking['analytics_account'] = value
        self.analytics_account_changed.emit(value)
        self._analytics_account = value

    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, value):
        value = value.strip()
        pattern = re.compile(AppConfig.regex_for_campaign_name_validation)
        result = bool(pattern.search(value))
        if not result:
            UserConfig.tracking['campaign_name'] = value
            self.campaign_name_changed.emit(value)
            self._campaign_name = value

    @property
    def webhook_url(self):
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, value):
        UserConfig.webhook_link = value
        self.webhook_url_changed.emit(value)
        self._webhook_url = value

    @property
    def target_blacklist(self):
        return self._target_blacklist

    @target_blacklist.setter
    def target_blacklist(self, value):
        target_blacklist = value
        target_blacklist = target_blacklist.strip().replace(" ", "")

        if target_blacklist:
            UserConfig.target_blacklist = list(filter(None, target_blacklist.split(",")))
            self.target_blacklist_changed.emit(value)
            self._target_blacklist = value
        else:
            UserConfig.target_blacklist = list()

