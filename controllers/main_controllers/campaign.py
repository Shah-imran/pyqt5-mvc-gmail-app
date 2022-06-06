from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from db.database import Database
from models.main_model import MainModel


class CampaignController(QObject):
    def __init__(self, model: MainModel, db: Database):
        super().__init__()

        self._model = model
        self._db = db

    @pyqtSlot(int)
    def number_of_accounts_update(self, value: int):
        self._model.campaign_model.number_of_accounts = value

    @pyqtSlot(int)
    def emails_per_account_update(self, value: int):
        self._model.campaign_model.emails_per_account = value

    @pyqtSlot(str)
    def delay_from(self, value: str):
        self._model.campaign_model.delay_from = int(value)

    @pyqtSlot(str)
    def delay_to(self, value: str):
        self._model.campaign_model.delay_to = int(value)
        
    @pyqtSlot(bool)
    def compose_plain_radio_selected(self, value: bool):
        self._model.campaign_model.compose_plain_radio = value
        
    @pyqtSlot(bool)
    def compose_html_radio_selected(self, value: bool):
        self._model.campaign_model.compose_html_radio = value

    @pyqtSlot(bool)
    def preview_checkbox_changed(self, value: bool):
        self._model.campaign_model.preview = value

    @pyqtSlot(bool)
    def custom_hostname_checkbox_update(self, value: bool):
        self._model.campaign_model.custom_hostname_checkbox = value

    @pyqtSlot(bool)
    def email_tracking_checkbox_update(self, value: bool):
        self._model.campaign_model.email_tracking_checkbox = value

    @pyqtSlot(bool)
    def webhook_checkbox_update(self, value: bool):
        self._model.campaign_model.webhook_checkbox = value

    @pyqtSlot(bool)
    def remove_targets_checkbox_update(self, value: bool):
        self._model.campaign_model.remove_targets_checkbox = value

    @pyqtSlot(bool)
    def check_for_blocks_checkbox_update(self, value: bool):
        self._model.campaign_model.check_for_blocks_checkbox = value

    @pyqtSlot(list)
    def attachments_update(self, value: list):
        self._model.campaign_model.attachments_list = self._model.campaign_model.attachments_list + value
        
    @pyqtSlot(str)
    def subject_update(self, value: str):
        self._model.campaign_model.subject = value
        
    @pyqtSlot(str)
    def body_update(self, value: str):
        if self._model.campaign_model.compose_plain_radio:
            self._model.campaign_model.plain_body = value
        else:
            self._model.campaign_model.html_body = value

    def set_progress_bar_value(self, value: int):
        self._model.campaign_model.progress_bar_value = value

    def campaign_status_text_update(self, value: str):
        self._model.campaign_model.campaign_status_text = value

    def campaign_label_text(self, value: str):
        self._model.campaign_model.campaign_label_text = value
