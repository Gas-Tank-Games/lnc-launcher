import os
import PyInstaller.__main__

print("build started")
PyInstaller.__main__.run(["lnc-launcher.py", "--windowed", "--onefile", "--console", "--icon=icon.ico"])
print("lnc launcher built")

# dependencies required
#
# - Python 3.13
# - pyinstaller
# - tkinter
# - terminal text effects