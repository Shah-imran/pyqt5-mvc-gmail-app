from typing import List, Any

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from views.main_app_screen import MainAppWindow
from views.inbox_screen import EmailStatus
from pyqtspinner.spinner import WaitingSpinner
from .tableView.db_tableView import TableModel, InLineEditDelegate
from config import AppConfig
from models.main_model import MainModel
from controllers.main_controller import MainController


class MainAppManager(MainAppWindow):
    def __init__(self, model: MainModel, main_controller: MainController):
        super().__init__()
        # self.handle_sidebar_btn_clicked(2)
        self.parents_for_spinner = {
            'self': self,
            'db_screen': self.db_screen,
            'inbox_screen': self.inbox_screen,
            'campaign_screen': self.campaign_screen,
            'configuration_screen': self.configuration_window
        }

        self._model = model
        self._main_controller = main_controller

        self.spinner = WaitingSpinner(self, True, True, Qt.ApplicationModal)

        # table view implemented
        self.db_table_model = TableModel(self._model.database_model.group_a,
                                         self._main_controller)

        self.db_screen.tableView.setModel(self.db_table_model)
        self.db_screen.tableView.show()
        self.db_screen.tableView.resizeColumnsToContents()

        delegate = InLineEditDelegate()
        self.db_screen.tableView.setItemDelegate(delegate)
        self.db_screen.groupa_radio.setChecked(True)

        # database module signals goes here
        self._model.database_model.update_db_tableview.connect(self.update_db_tableview)
        self.database_btn.clicked.connect(self.update_db_tableview)

        self.db_screen.groupa_radio.clicked.connect(self.update_db_tableview)
        self.db_screen.groupb_radio.clicked.connect(self.update_db_tableview)
        self.db_screen.target_radio.clicked.connect(self.update_db_tableview)
        self.db_screen.remove_btn.clicked.connect(self.db_tableview_remove_row)
        self.db_screen.add_btn.clicked.connect(self.db_table_model.insertRow)
        self.db_screen.import_btn.clicked.connect(
            self._main_controller.database_controller.import_data
        )
        self._model.database_model.set_group_a_checkbox.connect(
            self.db_screen.set_group_a_checkbox
        )
        self._model.database_model.set_group_b_checkbox.connect(
            self.db_screen.set_group_b_checkbox
        )
        self._model.database_model.set_target_checkbox.connect(
            self.db_screen.set_target_checkbox
        )
        self.db_screen.groupa_checkbox.stateChanged.connect(
            lambda: self._main_controller.database_controller.update_group_a_checkbox(
                self.db_screen.groupa_checkbox.isChecked()
            )
        )
        self.db_screen.groupb_checkbox.stateChanged.connect(
            lambda: self._main_controller.database_controller.update_group_b_checkbox(
                self.db_screen.groupb_checkbox.isChecked()
            )
        )
        self.db_screen.target_checkbox.stateChanged.connect(
            lambda: self._main_controller.database_controller.update_target_checkbox(
                self.db_screen.target_checkbox.isChecked()
            )
        )

        # to update model value
        self.db_screen.set_group_a_checkbox(True)

        # spinner signals
        signals = [self._main_controller.database_controller.spinner_control]
        for item in signals:
            item.connect(self.spinner_control)

        # configuration module signals
        self._model.configuration_model.analytics_account_changed.connect(
            self.configuration_window.set_analytics_account
        )
        self._model.configuration_model.campaign_name_changed.connect(
            self.configuration_window.set_campaign_name
        )
        self._model.configuration_model.webhook_url_changed.connect(
            self.configuration_window.set_webhook_url
        )
        self._model.configuration_model.target_blacklist_changed.connect(
            self.configuration_window.set_target_blacklist
        )
        self.configuration_window.analytics_account_lin.textChanged.connect(
            self._main_controller.configuration_controller.update_analytics_account
        )
        self.configuration_window.campaign_name_lin.textChanged.connect(
            self._main_controller.configuration_controller.update_campaign_name
        )
        self.configuration_window.webhook_url_lin.textChanged.connect(
            self._main_controller.configuration_controller.update_webhook_url
        )
        self.configuration_window.lineEdit_target_blacklist.textChanged.connect(
            self._main_controller.configuration_controller.update_target_blacklist
        )
        self.configuration_window.save_btn.clicked.connect(
            self._main_controller.configuration_controller.save_config
        )

        # inbox module signals
        self._model.inbox_model.date_changed.connect(self.inbox_screen.set_date)
        self.inbox_screen.dateEdit_imap.dateChanged.connect(
            lambda: self._main_controller.inbox_controller.update_imap_date(
                self.inbox_screen.dateEdit_imap.date().toString("M/d/yyyy")
            )
        )
        self.inbox_screen.a_radio_opt.toggled.connect(
            lambda: self._main_controller.inbox_controller.update_group_selection(
                self.inbox_screen.a_radio_opt.isChecked()
            )
        )
        self.inbox_screen.a_z_radio.toggled.connect(
            lambda: self._main_controller.inbox_controller.update_alphabetical_sort(
                self.inbox_screen.a_z_radio.isChecked()
            )
        )
        self.inbox_screen.latest_radio_opt.toggled.connect(
            lambda: self._main_controller.inbox_controller.update_date_sort(
                self.inbox_screen.latest_radio_opt.isChecked()
            )
        )
        self.inbox_screen.pushButton_download.clicked.connect(
            self._main_controller.inbox_controller.confirmation_window_for_download
        )

        self._main_controller.inbox_controller.show_download_dialog.connect(
            self.show_inbox_download_dialog
        )
        self._model.inbox_model.dialog_progressbar_value_changed.connect(
            self.inbox_screen.dialog.set_progressbar_value
        )
        self._model.inbox_model.dialog_label_text_changed.connect(
            self.inbox_screen.dialog.set_label_text
        )
        self.inbox_screen.dialog.pushButton_cancel.clicked.connect(
            lambda: self._main_controller.inbox_controller.download_dialog_button_action(
                self.inbox_screen.dialog.pushButton_cancel.text()
            )
        )
        self._main_controller.inbox_controller.change_download_dialog_button_text.connect(
            self.inbox_screen.dialog.change_button_text
        )
        self._main_controller.inbox_controller.close_download_dialog.connect(
            self.inbox_screen.dialog.close
        )
        self.inbox_screen.dialog.dialog_closed.connect(
            self._main_controller.inbox_controller.close_all_download_processes
        )
        self._main_controller.inbox_controller.spinner_control.connect(
            self.spinner_control
        )
        self._main_controller.inbox_controller.initialize_inbox_table.connect(
            lambda: self.inbox_screen.tableWidget.setRowCount(0)
        )
        self._model.inbox_model.change_new_email_count.connect(
            self.change_new_email_count
        )
        self._main_controller.inbox_controller.add_row_to_inbox_table.connect(
            self.add_row_to_inbox_table
        )
        self.inbox_screen.email_marked.connect(
            self._main_controller.inbox_controller.mark_email
        )
        self.inbox_screen.open_email.connect(
            self._main_controller.inbox_controller.open_email
        )
        self._model.inbox_model.to_email_lbl_changed.connect(
            self.inbox_screen.set_to_email_lbl
        )
        self._model.inbox_model.from_email_lbl_changed.connect(
            self.inbox_screen.set_from_email_lbl
        )
        self._model.inbox_model.email_topic_lbl_changed.connect(
            self.inbox_screen.set_email_topic_lbl
        )
        self._model.inbox_model.email_body_changed.connect(
            self.inbox_screen.set_email_body
        )
        self._model.inbox_model.email_body_font_size_changed.connect(
            self.inbox_screen.set_email_body_font_size
        )
        self.inbox_screen.inc_font_btn.clicked.connect(
            lambda: self._main_controller.inbox_controller.set_email_body_font_size(True)
        )
        self.inbox_screen.dec_font_btn.clicked.connect(
            lambda: self._main_controller.inbox_controller.set_email_body_font_size(False)
        )
        self.select_all_lbl.mousePressEvent = self._main_controller.inbox_controller.select_all
        self.trash_lbl.mousePressEvent = self.\
            _main_controller.inbox_controller.initiate_deleting_process

        # campaign page signals here
        # self._model.campaign_model.number_of_accounts_update.connect(
        #
        # )

    @pyqtSlot(object)
    def add_row_to_inbox_table(self, row: object):
        if 'row' in row:
            row_index = row['row']
        else:
            row_index = self.inbox_screen.tableWidget.rowCount()
            self.inbox_screen.tableWidget.insertRow(row_index)

        if "SEEN" == row['flag']:
            state = EmailStatus.readed
        else:
            state = EmailStatus.unRead

        self.inbox_screen.add_row(
                row_index, row['from_name'], row['subject'],
                str(row['date'].strftime("%b %d %Y %H:%M:%S")), row['uuid'], state)

    @pyqtSlot()
    def show_inbox_download_dialog(self):
        self.inbox_screen.dialog.exec_()

    @pyqtSlot(str)
    def spinner_control(self, parent=None):
        if parent:
            self.spinner = WaitingSpinner(self.parents_for_spinner[parent], True, True, Qt.ApplicationModal)
            self.spinner.start()
        else:
            self.spinner.stop()

    def db_tableview_remove_row(self):
        rows = self.db_screen.tableView.selectedIndexes()
        rows = list(set([item.row() for item in rows]))

        if len(rows) == 1:
            self._main_controller.database_controller.db_remove_row.emit(list(self.db_table_model._data.iloc[rows, 0]))
            self.db_table_model.db_remove_row.emit(rows[0])

        elif len(rows) > 1:
            ids = self.db_table_model._data[self.db_table_model._data.index.isin(rows)].iloc[:, 0].to_list()
            self._main_controller.database_controller.db_remove_row.emit(list(ids))
            self.db_table_model.db_remove_rows.emit(rows)

        else:
            print("Select something")

    @pyqtSlot()
    def update_db_tableview(self):
        self.db_table_model.layoutAboutToBeChanged.emit()

        if self.db_screen.groupa_radio.isChecked():
            self.db_table_model._data = self._model.database_model.group_a
            AppConfig.table_in_view = AppConfig.TableInView.group_a

        elif self.db_screen.groupb_radio.isChecked():
            self.db_table_model._data = self._model.database_model.group_b
            AppConfig.table_in_view = AppConfig.TableInView.group_b

        else:
            self.db_table_model._data = self._model.database_model.target
            AppConfig.table_in_view = AppConfig.table_in_view.target

        self.db_table_model.layoutChanged.emit()
        self.db_screen.tableView.resizeColumnsToContents()

    @pyqtSlot(int)
    def change_new_email_count(self, value: int):
        self.new_emails_count_lbl.setText(str(value))


if __name__ == "__main__":
    from assets import utils

    app = QtWidgets.QApplication([])
    utils.load_app_fonts()
    main_app = MainAppManager()
    main_app.showMaximized()
    app.exec_()
