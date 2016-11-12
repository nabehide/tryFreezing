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
            'dist_dir': 'dist\default',
        }
    },
    data_files=matplotlib.get_py2exe_datafiles(),

    zipfile=r'lib\library.zip',
    windows=['main.py']
)
