from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from .main_controllers.inbox import InboxController
from .main_controllers.campaign import CampaignController
from .main_controllers.database import DatabaseController
from .main_controllers.configuration import ConfigurationController
from models.main_model import MainModel
from db.database import Database
from config import UserConfig


class MainController(QObject):
    set_initial_value = pyqtSignal()

    def __init__(self, model: MainModel, db: Database):
        super().__init__()

        self._model = model
        self._db = db

        # initialize controllers here
        self.inbox_controller = InboxController(self._model, self._db)
        self.campaign_controller = CampaignController(self._model, self._db)
        self.database_controller = DatabaseController(self._model, self._db)
        self.configuration_controller = ConfigurationController(self._model)

        self.set_initial_value.connect(self._set_initial_value)

    @pyqtSlot()
    def _set_initial_value(self):
        self.configuration_controller.set_initial_value()
        self.inbox_controller.update_imap_date(UserConfig.imap_date)
