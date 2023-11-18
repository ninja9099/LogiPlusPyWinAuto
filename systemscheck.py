import pywinauto

print(pywinauto.sysinfo.is_x64_OS())
print(pywinauto.sysinfo.os_arch())
print(pywinauto.sysinfo.python_bitness())