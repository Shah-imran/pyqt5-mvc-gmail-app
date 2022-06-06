import pandas as pd
import os
from PyQt5.QtCore import pyqtSignal, QThread
from config import AppConfig, UserConfig
from db.database import Database


class FileLoading(QThread):
    loading_finished = pyqtSignal(object, str)

    def __init__(self, file_data: dict, db: Database):
        super().__init__()
        self.headers = dict(Group=['FIRSTFROMNAME', 'LASTFROMNAME', 'EMAIL',
                                   'EMAIL_PASS', 'PROXY:PORT', 'PROXY_USER', 'PROXY_PASS'],
                            Target=['1', '2', '3', '4', '5', '6', 'TONAME', 'EMAIL'])
        self.file_data = file_data
        self.file_path = ""
        self._db = db

    def run(self):
        for item in self.file_data.keys():
            self.file_path = f"{AppConfig.base_dir}/{item}.xlsx"
            if self.file_data[item]:
                if 'group' in item:
                    self.load_group_file(item)
                else:
                    self.load_target_file(item)

    def load_group_file(self, item):
        if os.path.exists(self.file_path):
            self._db.drop_group_table(group_name=item)
            data = self.read(self.file_path, sheet_name=item)

            data = data[self.headers['Group']]
            if not list(data.keys()) == self.headers['Group']:
                raise Exception(f"Group file headers not matching")

            data.fillna(' ', inplace=True)
            data = data.astype(str)
            data = data.loc[data['PROXY:PORT'] != ' ']

            if not len(data) > 0:
                raise Exception('No Data has been found')

            self._db.populate_groups(item, data)
            self.loading_finished.emit(pd.DataFrame(self._db.get_group_data(item)), item)
        else:
            raise Exception("File not found")

    def load_target_file(self, item):
        if os.path.exists(self.file_path):
            self._db.drop_target_table()
            data = self.read(self.file_path, sheet_name=item)

            data.columns = data.columns.astype(str)
            data = data[self.headers['Target']]
            if not list(data.keys()) == self.headers['Target']:
                raise Exception(f"Target file headers not matching")

            data.fillna(' ', inplace=True)
            data = data.astype(str)
            data = data.loc[data['EMAIL'] != ' ']

            # removing blacklisted targets

            if len(UserConfig.target_blacklist) > 0:
                data = data[~data['EMAIL'].str.lower(
                ).str.contains("|".join(UserConfig.target_blacklist))]

            if not len(data) > 0:
                # raise Exception('No Data has been found')
                print('No Data has been found')

            self._db.populate_targets(data)
            self.loading_finished.emit(pd.DataFrame(self._db.get_target_data()), item)
        else:
            raise Exception("File not found")

    @staticmethod
    def read(path_to_file: str, sheet_name: str) -> pd.DataFrame:
        return pd.read_excel(path_to_file, engine='openpyxl', sheet_name=sheet_name)
