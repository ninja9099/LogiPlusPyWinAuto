import time
from pywinauto.application import Application

# Start Notepad
app = Application(backend='uia').start("C:\Program Files\CPUID\ROG CPU-Z\cpuz.exe")

main_window = app['CPU-Z Dialog']
main_window.wait('visible', 10)
main_window.draw_outline()

# main_window.print_control_identifiers()

# main_window.ok.click()
# Steps
# 1 click on validate button to open a validate dialouge
main_window.Validate.click()


# main_window.print_control_identifiers()

# 2 get the pane in new window
new_pan = main_window["What is ValidationPane"]
new_pan.wait('visible', 10)


checkbox = new_pan.child_window(title=" Private validation", auto_id="1261", control_type="CheckBox")
checkbox.click_input()
new_pan.Close.click()