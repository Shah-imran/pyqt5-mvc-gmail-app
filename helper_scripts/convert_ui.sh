# ui files
pyuic5 forms/first_screen.ui -o views/generated/first_screen.py
pyuic5 forms/sign_in_screen.ui -o views/generated/sign_in_screen.py
pyuic5 forms/sign_up_screen.ui -o views/generated/sign_up_screen.py
pyuic5 forms/inbox_screen.ui -o views/generated/inbox_screen.py
pyuic5 forms/main_app_window.ui -o views/generated/main_app_window.py
pyuic5 forms/compaign_screen.ui -o views/generated/compaign_screen.py
pyuic5 forms/database_screen.ui -o views/generated/database_screen.py
pyuic5 forms/configurations_screen.ui -o views/generated/configurations_screen.py
pyuic5 forms/send_test_dialog.ui -o views/generated/send_test_dialog.py
pyuic5 forms/warm_up_module.ui -o views/generated/warm_up_module.py
pyuic5 forms/new_warmup_module.ui -o views/generated/new_warmup_module.py
pyuic5 forms/generic_progress_dialog.ui -o views/generated/generic_progress_dialog.py

# resources
pyrcc5 assets/app_resources.qrc -o app_resources_rc.py
