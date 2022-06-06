from .base import BaseThreadRequest
from PyQt5.QtCore import pyqtSignal, QThread
from .system_data import SystemInfo
from . import AppConfig


class Login(BaseThreadRequest, QThread):
    login_successful = pyqtSignal()
    login_failed = pyqtSignal(str)

    def __init__(self, email, password):
        kwargs = dict(api_endpoint=AppConfig.login_api_endpoint)
        super(Login, self).__init__(**kwargs)

        self.system_info = SystemInfo()
        self.machine_uuid = ''
        self.processor_id = ''
        self.email = email
        self.password = password

    def run(self) -> None:
        self.machine_uuid = self.system_info.machine_uuid
        self.processor_id = self.system_info.processor_id
        data = {
            'machine_uuid': self.system_info.machine_uuid,
            'processor_id': self.system_info.processor_id,
            'email': self.email,
            'password': self.password,
            'version': AppConfig.version,
            'type': 'main'
        }

        data = self.data_serialization(data)
        response = self.make_request(data)

        if len(response.text) > 100:
            self.login_failed.emit("Error at Authentication Server.\nContact Support")
        else:
            if response.text == 'Success':
                self.login_successful.emit()
            else:
                self.login_failed.emit(response.text)
