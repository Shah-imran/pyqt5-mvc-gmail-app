class UserConfiguration:
    imap_date = "8/24/2020"
    num_emails_per_address = 2
    delay_from = 10
    delay_to = 20
    limit_of_thread = 100
    login_email = ""
    tracking = {
            "analytics_account": "",
            "campaign_name": ""
        }

    webhook_link = ""
    compose_email_subject = "Just a friendly outreach about [3]"
    compose_email_body = '''{Hey|Hi|Hello} [TONAME],

    I'm reaching out to you because i {noticed|came across|found|visited} you website {the other day|yesterday} and thought you'd be interested in a {collaboration|partnership}.

    {Hope you don't mind my outreach!|Looking forward to your reply!}

    Regards,
    [FIRSTFROMNAME]'''
    compose_email_body_html = """\
    <html>
        <body>
            <p>{Hey|Hi|Hello} [TONAME],<br>
            I'm reaching out to you because i {noticed|came across|found|visited} you website {the other day|yesterday} and thought you'd be interested in a {collaboration|partnership}.<br>
            {Hope you don't mind my outreach!|Looking forward to your reply!}<br>
            </p>
        </body>
    </html>
    """
    body_type = "Normal"

    check_for_blocks = False
    target_blacklist = list()

    def __init__(self):
        pass
