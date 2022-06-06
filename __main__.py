import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from assets import utils
from view_managers.login_dialog_manager import LoginDialogManager
from view_managers.main_app_manager import MainAppManager
from models.authentication_model import AuthenticationModel
from models.main_model import MainModel
from controllers.authentication_controller import AuthenticationController
from controllers.main_controller import MainController
from db.database import Database
from config import AppConfig
from win32event import CreateMutex
from win32api import CloseHandle, GetLastError
from winerror import ERROR_ALREADY_EXISTS


class SingleInstance:
    """ Limits application to single instance """

    def __init__(self):
        self.mutexname = "testmutex_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}"
        self.mutex = CreateMutex(None, False, self.mutexname)
        self.lasterror = GetLastError()

    def already_running(self):
        return self.lasterror == ERROR_ALREADY_EXISTS

    def __del__(self):
        if self.mutex:
            CloseHandle(self.mutex)


class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        utils.load_app_fonts()

        self.db = Database()

        # models and controller initialization
        self.auth_model = AuthenticationModel()
        self.auth_controller = AuthenticationController(self.auth_model)
        self.auth_controller.load_config()

        self.main_model = MainModel()
        self.main_controller = MainController(self.main_model, self.db)

        # gui initialization goes here
        self.login_dialog = LoginDialogManager(self.auth_model, self.auth_controller)
        self.main_window = MainAppManager(self.main_model, self.main_controller)

        is_testing_environment = 0
        try:
            if os.getenv('fa414ce5-05d1-45e2-ba53-df760ad35fa0'):
                is_testing_environment = int(os.getenv('fa414ce5-05d1-45e2-ba53-df760ad35fa0'))
        except:
            pass

        if not is_testing_environment:
            self.login_dialog.show()
            self.auth_controller.checking_for_update()
            self.auth_controller.login_accepted.connect(self.open_main_window)
        else:
            self.open_main_window()

        # Signals goes here

    @pyqtSlot()
    def open_main_window(self):
        """ when login try is successful emit
        loginAccepted signal which closes itself
        and opens the main window """
        self.main_controller.database_controller.startup_db_loading.emit()
        # self.main_controller.configuration_controller.set_initial_value()
        self.main_controller.set_initial_value.emit()
        self.login_dialog.login_accepted.emit()
        self.main_window.show()
        print("Login accepted")


if __name__ == "__main__":
    # do this at beginnig of your application
    myapp = SingleInstance()

    # check is another instance of same program running
    if myapp.already_running():
        print("Another instance of this program is already running")
        sys.exit(1)

    app = App(sys.argv)

    sys.exit(app.exec_())
