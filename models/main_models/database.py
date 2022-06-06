from PyQt5.QtCore import QObject, pyqtSignal
import pandas as pd


class DatabaseModel(QObject):
    update_db_tableview = pyqtSignal()
    set_group_a_checkbox = pyqtSignal(bool)
    set_group_b_checkbox = pyqtSignal(bool)
    set_target_checkbox = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.group_a = pd.DataFrame()
        self.group_b = pd.DataFrame()
        self.target = pd.DataFrame()

        self._group_a_checkbox: bool = False
        self._group_b_checkbox: bool = False
        self._target_checkbox: bool = False

        # self._group_a = pd.DataFrame()
        # self._group_b = pd.DataFrame()
        # self._target = pd.DataFrame()

    @property
    def group_a_checkbox(self):
        return self._group_a_checkbox

    @group_a_checkbox.setter
    def group_a_checkbox(self, value: bool):
        self.set_group_a_checkbox.emit(value)
        self._group_a_checkbox = value

    @property
    def group_b_checkbox(self):
        return self._group_b_checkbox

    @group_b_checkbox.setter
    def group_b_checkbox(self, value: bool):
        self.set_group_b_checkbox.emit(value)
        self._group_b_checkbox = value

    @property
    def target_checkbox(self):
        return self._target_checkbox

    @target_checkbox.setter
    def target_checkbox(self, value: bool):
        self.set_target_checkbox.emit(value)
        self._target_checkbox = value

    # @property
    # def group_a(self):
    #     return self._group_a
    #
    # @group_a.setter
    # def group_a(self, df):
    #     self.update_db_tableView.emit()
    #     self._group_a = df
    #
    # @property
    # def group_b(self):
    #     return self._group_b
    #
    # @group_b.setter
    # def group_b(self, df):
    #     self._group_b = df
    #
    # @property
    # def target(self):
    #     return self._target
    #
    # @target.setter
    # def target(self, df):
    #     self._target = df
