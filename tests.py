from pywinauto.application import Application

# Start Notepad
app = Application(backend='uia').start("C:\Program Files\LogiOptionsPlus\logioptionsplus.exe")
app = app.connect(title=u'Logi Options+', timeout=10)

app.LogiOptionsPlus.print_control_identifiers()
main_window = app.LogioOptionsPlus.child_window(auto_id="389328", control_type="Document").wrapper_object()

add_device_button = app.LogioOptionsPlus.child_window(title="ADD DEVICE", auto_id="icon-add", control_type="Button").wrapper_object()
add_device_button.click_input()


import pdb
pdb.set_trace()