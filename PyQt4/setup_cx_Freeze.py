# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

build_exe = {
    "optimize": 2,
    "excludes": {"collections.abc", "_ssl", "Tkinter", "Tcl", "Tk", "PIL"},
}

setup(name="",
      version="1.0",
      description='',
      options={"build_exe": build_exe},
      executables=[Executable("main.py", base=base)])
