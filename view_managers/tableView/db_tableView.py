import typing

from PyQt5.QtCore import QAbstractTableModel, Qt, pyqtSignal, pyqtSlot, QModelIndex
from PyQt5 import QtWidgets


class TableModel(QAbstractTableModel):
    db_remove_row = pyqtSignal(int)
    db_remove_rows = pyqtSignal(object)

    def __init__(self, data, main_controller):
        super().__init__()

        self._data = data
        self._main_controller = main_controller
        self.db_remove_row.connect(self.removeRow)
        self.db_remove_rows.connect(self.removeRows)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self._data.shape[0]

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self._data.shape[1]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        """
        Make table editable.
        make first column non editable
        :param index:
        :return:
        """
        if index.column() > 0:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        else:
            return Qt.ItemIsSelectable

    def setData(self, index: QModelIndex, value: typing.Any, role: int = Qt.EditRole) -> bool:
        """
                Edit data in table cells
                :param index:
                :param value:
                :param role:
                :return:
        """
        if index.isValid():
            row = self._data.iloc[index.row()].to_dict()
            row[str(self._data.columns[index.column()])] = value

            if self._data.iloc[index.row(), index.column()] != value:
                self._main_controller.database_controller.db_update_row.emit(row)
                self._data.iloc[index.row(), index.column()] = value
                self.dataChanged.emit(
                    index, index, (Qt.DisplayRole,))
                return True

        return False

    def insertRow(self) -> bool:
        row_count = self.rowCount()
        self.beginInsertRows(QModelIndex(), row_count, row_count)
        result, o_id = self._main_controller.database_controller.db_insert_row()
        if result:
            self._data.loc[row_count] = [o_id] + \
                                        [""] * (self._data.shape[1] - 1)
            row_count += 1
            self.endInsertRows()
            return True
        else:
            return False

    @pyqtSlot(int)
    def removeRow(self, position):
        row_id = position
        # result = self._main_controller.db_remove_row.emit(int(self._data.iloc[row_id, 0]))
        # if result:
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QModelIndex(),
                             row_count, row_count)
        self._data.drop(row_id, axis=0, inplace=True)
        self._data.reset_index(drop=True, inplace=True)
        self.endRemoveRows()
        return True

    @pyqtSlot(object)
    def removeRows(self, rows) -> bool:
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QModelIndex(),
                             row_count, row_count)
        self._data.drop(rows, inplace=True)
        self._data.reset_index(drop=True, inplace=True)
        self.endRemoveRows()
        return True


class InLineEditDelegate(QtWidgets.QItemDelegate):
    """
    Delegate is important for inline editing of cells
    """

    def createEditor(self, parent, option, index):
        return super(InLineEditDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        text = index.data(Qt.EditRole) or index.data(
            Qt.DisplayRole)
        editor.setText(str(text))
