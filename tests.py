from pywinauto.application import Application
import time
# Start Notepad
app = Application(backend='uia').start("C:\Program Files\LogiOptionsPlus\logioptionsplus.exe")
# app = app.connect(title=u'Logi Options+', timeout=10)

time.sleep(10)
main_window = app.LogioOptionsPlus.child_window(title="ADD DEVICE", control_type="Button").wrapper_object()

main_window.click_input()

# print control identifier of the new window by keeping the that window open
# so the control identifer are current state for the application
app.LogiOptionsPlus.print_control_identifiers()