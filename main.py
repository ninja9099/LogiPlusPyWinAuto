import time
from pywinauto import application
from pywinauto.findwindows import ElementNotFoundError


class BestRx:
    def __init__(self, app_path):
        self.app_path = app_path
        self.app = None
        self.main_dlg = None

    def start_app(self):
        try:
            self.app = application.Application(backend='uia').start(self.app_path)
            time.sleep(5)
            self.main_dlg = self.app.LogioOptionsPlus
        except FileNotFoundError:
            print("File not found.")
        except ElementNotFoundError:
            print("Main window not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_button(self, button_name):
        try:
            button = self.main_dlg.child_window(title_re=button_name, control_type="Button")
            if button.exists():
                button.click_input()
            else:
                print(f"Button '{button_name}' not found.")
        except ElementNotFoundError:
            print(f"Button '{button_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_app(self):
        if self.app:
            self.app.kill()

app_path  = "C:\Program Files\LogiOptionsPlus\logioptionsplus.exe"
bestRx = BestRx(app_path)
bestRx.start_app()

bestRx.click_button("ADD DEVICE")
# bestRx.close_app()