from .base import BaseThreadRequest
from PyQt5.QtCore import pyqtSignal, QThread
import requests
from . import AppConfig


class UpdateChecker(BaseThreadRequest, QThread):
    label_update = pyqtSignal(str)
    progressbar_update = pyqtSignal(int)
    update_checked = pyqtSignal()

    def __init__(self):
        kwargs = dict(api_endpoint=AppConfig.update_checker_api_endpoint)
        super(UpdateChecker, self).__init__(**kwargs)

    def run(self) -> None:
        response = self.make_request(None, timeout=10)
        response = response.json()
        if not response['update_needed']:
            self.label_update.emit("Update checking finished. Now you can login.")
            self.progressbar_update.emit(100)
            self.update_checked.emit()
