# -*- coding: utf-8 -*-
from distutils.core import setup
import sys
import py2exe
import matplotlib
sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {
            'bundle_files': 3,
            'optimize': 2,
            'compressed': 2,
            'excludes': ['PIL', 'scipy', 'tk', 'lxml', 'sqlite3', 'test',
                         'pydoc', '_agg2', '_cario', '_cocoaagg',
                         'matplotlib.numerix.fft', "PyQt4._qt",
                         "matplotlib.numerix.linear_algebra",
                         "matplotlib.numerix.random_array", '_fltkagg',
                         '_gtk', '_gtkcairo', '_gtkagg', '_ssl', '_tkagg',
                         'bsddb', 'curses', 'doctest', 'email', 'pdb',
                         'pyreadline', 'pywin.debugger', 'pywin.debugger.dbgcon',
                         'pywin.dialogs', 'tcl', 'Tkconstants', 'Tkinter'],
            'dll_excludes': ['libpng16.dll', 'tcl85.dll', 'tk85.dll',
                             'libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll'],
            'dist_dir': 'dist\customized',
        }
    },
    data_files=matplotlib.get_py2exe_datafiles(),

    zipfile=r'lib\library.zip',
    windows=['main.py']
)
