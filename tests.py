from pywinauto.application import Application
import time
# Start Notepad
app = Application(backend='uia').start("C:\Program Files\LogiOptionsPlus\logioptionsplus.exe")
# app = app.connect(title=u'Logi Options+', timeout=10)

time.sleep(10)
main_window = app.LogioOptionsPlus.child_window(title_re="ADD DEVICE", control_type="Button").wrapper_object()

main_window.click_input()

bluetooth_button = app.LogioOptionsPlus.child_window(title="receiver-icon Bluetooth ", auto_id="Bluetooth-connection-info-container", control_type="Button").wrapper_object()
# print control identifier of the new window by keeping the that window open
# so the control identifer are current state for the application
bluetooth_button.click_input()

app.LogiOptionsPlus.print_control_identifiers()