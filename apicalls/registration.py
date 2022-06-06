from .base import BaseThreadRequest
from PyQt5.QtCore import pyqtSignal, QThread
from .system_data import SystemInfo
from . import AppConfig


class SignUp(BaseThreadRequest, QThread):
    sign_up_successful = pyqtSignal(str)
    sign_up_failed = pyqtSignal(str)

    def __init__(self, email, password):
        kwargs = dict(api_endpoint=AppConfig.sign_up_api_endpoint)
        super(SignUp, self).__init__(**kwargs)

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
            self.sign_up_failed.emit("Error at Authentication Server.\nContact Support")
        else:
            self.sign_up_failed.emit(response.text)
