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
            print("this are the list of windows we have for app ", self.app.windows())
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

app_path  = "C:\Program Files\CPUID\ROG CPU-Z\cpuz.exe"
bestRx = BestRx(app_path)
bestRx.start_app()
import pdb
pdb.set_trace()

bestRx.close_app()