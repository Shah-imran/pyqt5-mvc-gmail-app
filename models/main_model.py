from PyQt5.QtCore import QObject, pyqtSignal
from .main_models.inbox import InboxModel
from .main_models.campaign import CampaignModel
from .main_models.database import DatabaseModel
from .main_models.configuration import ConfigurationModel


class MainModel(QObject):

    def __init__(self):
        super().__init__()

        self.inbox_model = InboxModel()
        self.campaign_model = CampaignModel()
        self.database_model = DatabaseModel()
        self.configuration_model = ConfigurationModel()




