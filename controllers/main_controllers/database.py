from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from threading import Thread
from config import AppConfig
import pandas as pd
from controllers.main_controllers.file_loading.excel_loading import FileLoading
from db.database import Database
from models.main_model import MainModel


class DatabaseController(QObject):
    startup_db_loading = pyqtSignal()
    db_update_row = pyqtSignal(dict)
    db_remove_row = pyqtSignal(object)
    spinner_control = pyqtSignal(str)

    def __init__(self, model: MainModel, db: Database):
        super().__init__()

        self._model: MainModel = model
        self._db: Database = db

        # connect signals here

        self.startup_db_loading.connect(self._startup_db_load)
        self.db_update_row.connect(self._db_update_row)
        self.db_remove_row.connect(self._db_remove_row)

        # stop spinner
        self._db.removing_finished.connect(lambda: self.spinner_control.emit(None))

    def update_group_a_checkbox(self, value):
        self._model.database_model.group_a_checkbox = value

    def update_group_b_checkbox(self, value):
        self._model.database_model.group_b_checkbox = value

    def update_target_checkbox(self, value):
        self._model.database_model.target_checkbox = value

    def import_data(self):
        checkbox_data = {
            'group_a': self._model.database_model.group_a_checkbox,
            'group_b': self._model.database_model.group_b_checkbox,
            'target': self._model.database_model.target_checkbox
        }

        self.file_loading = FileLoading(checkbox_data, self._db)
        self.file_loading.loading_finished.connect(self.update_db_tableview_models)
        self.file_loading.finished.connect(self.update_db_tableview)
        self.file_loading.finished.connect(self.file_loading.quit)
        self.file_loading.finished.connect(self.file_loading.deleteLater)
        self.file_loading.start()
        self.spinner_control.emit('self')

    @pyqtSlot(object, str)
    def update_db_tableview_models(self, data: pd.DataFrame, table_name: str):
        if table_name == AppConfig.TableInView.group_a.name:
            self._model.database_model.group_a = data
        elif table_name == AppConfig.TableInView.group_b.name:
            self._model.database_model.group_b = data
        else:
            self._model.database_model.target = data

    @pyqtSlot()
    def update_db_tableview(self):
        self._model.database_model.update_db_tableview.emit()
        self.spinner_control.emit(None)

    @pyqtSlot()
    def _startup_db_load(self):
        self._db.fill_up_database_if_empty()
        self._model.database_model.group_a = pd.DataFrame(self._db.get_group_data('group_a'))
        self._model.database_model.group_b = pd.DataFrame(self._db.get_group_data('group_b'))
        self._model.database_model.target = pd.DataFrame(self._db.get_target_data())

    def db_insert_row(self) -> tuple:
        result, o_id = self._db.insert_row(table=self.get_db_table_name(exact=True))
        return result, o_id

    @pyqtSlot(object)
    def _db_remove_row(self, ids) -> None:
        self.spinner_control.emit('self')
        Thread(target=self.__db_remove_row, daemon=True, args=[ids, ]).start()

    def __db_remove_row(self, ids):
        self._db.remove(table=self.get_db_table_name(), ids=ids)

    @pyqtSlot(dict)
    def _db_update_row(self, row: dict):
        Thread(target=self.__db_update_row, daemon=True, args=[row, ]).start()

    def __db_update_row(self, row: dict):
        self._db.update_row(table=self.get_db_table_name(), row=row)

    @staticmethod
    def get_db_table_name(exact: bool = False) -> str:
        group_a = AppConfig.TableInView.group_a == AppConfig.table_in_view
        group_b = AppConfig.TableInView.group_b == AppConfig.table_in_view
        if group_a or group_b:
            if exact:
                return "group_a" if group_a else "group_b"
            else:
                return "group"
        else:
            return "target"
