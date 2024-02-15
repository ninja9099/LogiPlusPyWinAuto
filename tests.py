import time
from pywinauto.application import Application

# Start Notepad
app = Application(backend='uia').start("C:\Program Files\CPUID\ROG CPU-Z\cpuz.exe")

main_window = app['CPU-Z Dialog']
main_window.wait('visible', 10)
main_window.draw_outline()

main_window.print_control_identifiers()

import pdb
pdb.set_trace()

main_window.ok.click()
