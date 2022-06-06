import pandas as pd
from PyQt5.QtCore import QObject, pyqtSignal
from .tables import Group, Target, engine
from sqlalchemy.orm import sessionmaker
from customexceptions.base import ArgumentMissing


def object_as_dict(query):
    return [u.__dict__ for u in query.all()]


class Database(QObject):
    removing_finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        _session = sessionmaker(bind=engine)
        self._session = _session()
        self.table = {
            "group": Group,
            "target": Target
        }

    def remove(self, table: str = None, ids: list = None) -> bool:
        """remove row from table by id and this method expects
                two arguments table and id of that row"""

        if table is not None and ids is not None:
            for _id in ids:
                objects = self._session.query(self.table[table]).get(int(_id))
                if objects:
                    self._session.delete(objects)
                    self._session.commit()

            self.removing_finished.emit()
            return True
        else:
            raise ArgumentMissing('Must provide table name and id list')

    def populate_groups(self, group: str, data: pd.DataFrame):
        """ populate table Group """
        objects = [Group(
            first_from_name=row['FIRSTFROMNAME'],
            last_from_name=row['LASTFROMNAME'],
            email=row['EMAIL'],
            email_pass=row['EMAIL_PASS'],
            proxy_port=row['PROXY:PORT'],
            proxy_user=row['PROXY_USER'],
            proxy_pass=row['PROXY_PASS'],
            group_name=group
        ) for index, row in data.iterrows()]

        self._session.add_all(objects)
        self._session.commit()
        return True

    def populate_targets(self, data: pd.DataFrame):
        """ populate table Target """
        objects = [Target(
            one=row['1'],
            two=row['2'],
            three=row['3'],
            four=row['4'],
            five=row['5'],
            six=row['6'],
            to_name=row['TONAME'],
            email=row['EMAIL']
        ) for index, row in data.iterrows()]

        self._session.add_all(objects)
        self._session.commit()
        return True

    def insert_row(self, table: str = None) -> tuple:
        """ add row to table with this method and it expects
        table name and rows as dict"""
        if "group" in table:
            objects = Group(
                first_from_name="",
                last_from_name="",
                email="",
                email_pass="",
                proxy_port="",
                proxy_user="",
                proxy_pass="",
                group_name=table
            )
        else:
            objects = Target(
                one="",
                two="",
                three="",
                four="",
                five="",
                six="",
                to_name="",
                email=""
            )

        self._session.add(objects)
        self._session.commit()
        return True, objects.id

    def update_row(self, table: str = None, row: dict = None):
        if "group" in table:
            objects = self._session.query(Group).get(int(row['ID']))
            objects.first_from_name = row["FIRSTFROMNAME"]
            objects.last_from_name = row["LASTFROMNAME"]
            objects.email = row["EMAIL"]
            objects.email_pass = row["EMAIL_PASS"]
            objects.proxy_port = row["PROXY:PORT"]
            objects.proxy_user = row["PROXY_USER"]
            objects.proxy_pass = row["PROXY_PASS"]

        else:
            objects = self._session.query(Target).get(int(row['ID']))
            objects.one = row["1"]
            objects.two = row["2"]
            objects.three = row["3"]
            objects.four = row["4"]
            objects.five = row["5"]
            objects.six = row["6"]
            objects.to_name = row["TONAME"]
            objects.email = row["EMAIL"]

        self._session.commit()
        print("db updated")

    def drop_group_table(self, group_name: str = None) -> bool:
        self._session.query(Group).filter(Group.group_name == group_name).delete()
        self._session.commit()

    def drop_target_table(self):
        self._session.query(Target).delete()
        self._session.commit()

    def drop_all_table(self):
        pass

    def add_table(self):
        pass

    def fill_up_database_if_empty(self):
        group_a = True if not self._session.query(Group).first() else False
        group_b = True if not self._session.query(Group).first() else False
        target = True if not self._session.query(Target).first() else False

        self.dummy_data_db(group_a=group_a, group_b=group_b, target=target)

    def get_group_data(self, group: str = None) -> list:
        """ it will return a list of dict"""
        if group:
            results = self._session.query(Group).filter(Group.group_name == group).all()
            return [{
                        'ID': item.id,
                        'FIRSTFROMNAME': item.first_from_name,
                        'LASTFROMNAME': item.last_from_name,
                        'EMAIL': item.email,
                        'EMAIL_PASS': item.email_pass,
                        'PROXY:PORT': item.proxy_port,
                        'PROXY_USER': item.proxy_user,
                        'PROXY_PASS': item.proxy_pass
                    }.copy() for item in results]
        else:
            raise ArgumentMissing('Group selecting string not given')

    def get_target_data(self) -> list:
        results = self._session.query(Target).all()
        return [{
                    'ID': item.id,
                    '1': item.one,
                    '2': item.two,
                    '3': item.three,
                    '4': item.four,
                    '5': item.five,
                    '6': item.six,
                    'TONAME': item.to_name,
                    'EMAIL': item.email
                }.copy() for item in results]

    def dummy_data_db(self, group_a=True, group_b=True, target=True) -> None:
        group_id = 0
        if group_a:
            group_id = group_id + 1
            objects = Group(
                id=group_id,
                first_from_name="",
                last_from_name="",
                email="",
                email_pass="",
                proxy_port="",
                proxy_user="",
                proxy_pass="",
                group_name="group_a"
            )
            self._session.add(objects)

        if group_b:
            group_id = group_id + 1
            objects = Group(
                id=group_id,
                first_from_name="",
                last_from_name="",
                email="",
                email_pass="",
                proxy_port="",
                proxy_user="",
                proxy_pass="",
                group_name="group_b"
            )
            self._session.add(objects)

        if target:
            objects = Target(
                id=1,
                one="",
                two="",
                three="",
                four="",
                five="",
                six="",
                to_name="",
                email=""
            )
            self._session.add(objects)

        self._session.commit()
