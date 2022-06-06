from PyQt5.QtCore import QObject, pyqtSignal
from config import UserConfig


class CampaignModel(QObject):
    group_a_selected = pyqtSignal(bool)
    group_b_selected = pyqtSignal(bool)
    number_of_accounts_update = pyqtSignal(int)
    emails_per_account_update = pyqtSignal(int)
    delay_from = pyqtSignal(int)
    delay_to = pyqtSignal(int)
    compose_plain_radio_selected = pyqtSignal(bool)
    compose_html_radio_selected = pyqtSignal(bool)
    preview_checkbox_changed = pyqtSignal(bool)
    custom_hostname_checkbox_update = pyqtSignal(bool)
    email_tracking_checkbox_update = pyqtSignal(bool)
    webhook_checkbox_update = pyqtSignal(bool)
    remove_targets_update = pyqtSignal(bool)
    check_for_blocks_checkbox_update = pyqtSignal(bool)
    attachments_update = pyqtSignal(list)
    subject_update = pyqtSignal(str)
    body_update = pyqtSignal(str, int)
    campaign_button_update = pyqtSignal(bool)
    progress_bar_value_changed = pyqtSignal(int)
    campaign_status_text_changed = pyqtSignal(str)
    campaign_label_text_changed = pyqtSignal(str)
    error_report_to_controller = pyqtSignal(str, str)

    @property
    def number_of_accounts(self):
        return self._number_of_accounts

    @number_of_accounts.setter
    def number_of_accounts(self, value):
        self._number_of_accounts = value

    @property
    def emails_per_account(self) -> int:
        return self._emails_per_account

    @emails_per_account.setter
    def emails_per_account(self, value: int):
        self._emails_per_account = value

    @property
    def delay_from(self) -> int:
        return self._delay_from

    @delay_from.setter
    def delay_from(self, value: int):
        self._delay_from = value

    @property
    def delay_to(self) -> int:
        return self._delay_to

    @delay_from.setter
    def delay_to(self, value: int):
        self._delay_to = value

    @property
    def compose_plain_radio(self) -> bool:
        return self._compose_plain_radio

    @compose_plain_radio.setter
    def compose_plain_radio(self, value: bool):
        self._compose_plain_radio = value

    @property
    def compose_html_radio(self) -> bool:
        return self._compose_html_radio

    @compose_html_radio.setter
    def compose_html_radio(self, value: bool):
        self._compose_html_radio = value

    @property
    def preview(self) -> bool:
        return self._preview

    @preview.setter
    def preview(self, value: bool):
        self._preview = value

    @property
    def custom_hostname_checkbox(self) -> bool:
        return self._custom_hostname_checkbox

    @custom_hostname_checkbox.setter
    def custom_hostname_checkbox(self, value: bool):
        self._custom_hostname_checkbox = value

    @property
    def email_tracking_checkbox(self) -> bool:
        return self._email_tracking_checkbox

    @email_tracking_checkbox.setter
    def email_tracking_checkbox(self, value: bool):
        self._email_tracking_checkbox = value

    @property
    def webhook_checkbox(self) -> bool:
        return self._webhook_checkbox

    @webhook_checkbox.setter
    def webhook_checkbox(self, value: bool):
        self._webhook_checkbox = value

    @property
    def remove_targets_checkbox(self) -> bool:
        return self._remove_targets_checkbox

    @remove_targets_checkbox.setter
    def remove_targets_checkbox(self, value: bool):
        self._remove_targets_checkbox = value

    @property
    def check_for_blocks_checkbox(self) -> bool:
        return self._check_for_blocks_checkbox

    @check_for_blocks_checkbox.setter
    def check_for_blocks_checkbox(self, value: bool):
        self._check_for_blocks_checkbox = value

    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, value: str):
        self._subject = value

    @property
    def plain_body(self) -> str:
        return self._plain_body

    @plain_body.setter
    def plain_body(self, value: str):
        self._plain_body = value

    @property
    def html_body(self) -> str:
        return self._html_body

    @html_body.setter
    def html_body(self, value: str):
        self._html_body = value

    @property
    def campaign_running(self) -> bool:
        return self._campaign_running

    @campaign_running.setter
    def campaign_running(self, value: bool):
        self._campaign_running = value

    @property
    def progress_bar_value(self) -> int:
        return self._progress_bar_value

    @progress_bar_value.setter
    def progress_bar_value(self, value: int):
        self._progress_bar_value = value

    @property
    def campaign_status_text(self) -> str:
        return self._campaign_status_text

    @campaign_status_text.setter
    def campaign_status_text(self, value: str):
        self._campaign_status_text = value

    @property
    def campaign_label_text(self) -> str:
        return self._campaign_label_text

    @campaign_label_text.setter
    def campaign_label_text(self, value: str):
        self._campaign_label_text = value
        
    @property
    def group_a(self) -> bool:
        return self._group_a
    
    @group_a.setter
    def group_a(self, value: bool):
        self._group_a = value
    
    @property
    def group_b(self) -> bool:
        return self._group_b
    
    @group_b.setter
    def group_b(self, value: bool):
        self._group_b = value

    def __init__(self):
        super().__init__()

        self._group_a = True
        self._group_b = False
        self._number_of_accounts = UserConfig.limit_of_thread
        self._emails_per_account = UserConfig.num_emails_per_address
        self._delay_from = UserConfig.delay_from
        self._delay_to = UserConfig.delay_to
        self._compose_plain_radio = True
        self._compose_html_radio = False
        self._preview = False
        self._custom_hostname_checkbox = False
        self._email_tracking_checkbox = False
        self._webhook_checkbox = False
        self._remove_targets_checkbox = False
        self._check_for_blocks_checkbox = UserConfig.check_for_blocks
        self._attachments_list = []
        self._subject = UserConfig.compose_email_subject
        self._plain_body = UserConfig.compose_email_body
        self._html_body = UserConfig.compose_email_body_html
        self._campaign_running = False
        self._progress_bar_value: int = 0
        self._campaign_status_text = ""
        self._campaign_label_text = ""
