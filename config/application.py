from enum import Enum
from socks import PROXY_TYPE_SOCKS5


class AppConfiguration:
    base_api = 'https://enzim.pythonanywhere.com/'
    test_base_api = "http://127.0.0.1:5000/"
    version = "2.2r"
    update_checker_api_endpoint = f"version/{version}"
    login_api_endpoint = f"login"
    sign_up_api_endpoint = f"register"

    regex_for_email_validation = r"[^@]+@[^@]+\.[^@]+"
    regex_for_campaign_name_validation = "[^a-zA-Z0-9_ ]+"

    base_dir = 'database'
    log_filename = "app"
    group_a_file_path = f"{base_dir}/group_a.xlsx"
    group_b_file_path = f"{base_dir}/group_b.xlsx"
    target_file_path = f"{base_dir}/target.xlsx"

    imap_server = 'imap.gmail.com'
    imap_port = 993
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    proxy_type = PROXY_TYPE_SOCKS5

    class TableInView(Enum):
        group_a = 0
        group_b = 1
        target = 2

    table_in_view = TableInView.group_a  # group_a, group_b, target

    inbox_page_email_body_font_size_min = 2

    def __init__(self):
        pass
