from . import AppConfig, UserConfig
from PyQt5.QtCore import QThread, pyqtSignal
import json


class ConfigManager(QThread):
    loading_finished = pyqtSignal()

    def __init__(self, method: str):
        super().__init__()
        self.methods_list = {
            'save': self.save_config_json,
            'load': self.load_config_json
        }
        self.method_to_run = self.methods_list[method]

    def run(self):
        self.method_to_run()

    @staticmethod
    def save_config_json():
        try:
            data = {
                "config":
                    {
                        "date": UserConfig.imap_date,
                        "num_emails_per_address": UserConfig.num_emails_per_address,
                        "delay_from": UserConfig.delay_from,
                        "delay_to": UserConfig.delay_to,
                        "limit_of_thread": UserConfig.limit_of_thread,
                        "compose_email_subject": UserConfig.compose_email_subject,
                        "compose_email_body": UserConfig.compose_email_body,
                        "compose_email_body_html": UserConfig.compose_email_body_html,
                        "login_email": UserConfig.login_email,
                        "tracking": UserConfig.tracking,
                        "webhook_link": UserConfig.webhook_link,
                        "check_for_blocks": UserConfig.check_for_blocks,
                        "target_blacklist": UserConfig.target_blacklist
                    }
            }
            with open(AppConfig.base_dir + '/config.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as e:
            print("Exception occurred at update_config_json : {}".format(e))

    def load_config_json(self):
        try:
            with open('{}/config.json'.format(AppConfig.base_dir)) as json_file:
                data = json.load(json_file)
            config = data['config']
            UserConfig.imap_date = config['date']
            if config['compose_email_subject']:
                UserConfig.compose_email_subject = config['compose_email_subject']
            if config['compose_email_body']:
                UserConfig.compose_email_body = config['compose_email_body']
            if config['compose_email_body_html']:
                UserConfig.compose_email_body_html = config['compose_email_body_html']
            UserConfig.num_emails_per_address = config['num_emails_per_address']
            UserConfig.delay_from = config['delay_from']
            UserConfig.delay_to = config['delay_to']
            UserConfig.limit_of_thread = config['limit_of_thread']
            UserConfig.login_email = config['login_email']
            UserConfig.tracking = config['tracking']
            UserConfig.webhook_link = config['webhook_link']
            UserConfig.check_for_blocks = config['check_for_blocks']
            UserConfig.target_blacklist = config['target_blacklist']
            self.loading_finished.emit()
        except Exception as e:
            print("Exception occurred at config loading : {}".format(e))
