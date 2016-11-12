# tryFreezeing
This is sample code for freezing.
* py2exe
* PyInstaller
* cx_Freeze

## env
* Windows7 32bit professional
* CPU : Core-i5-4310U 2.00GHz
* RAM : 4GB

## python evb
* python 2.7.12
* numpy 1.11.2
* matplotlib 1.5.1
* pyqt 4.11.4
* py2exe 0.6.9
* PyInstaller 3.2.dev0+483c819
* cx_Freeze 4.3.4

## How to execute
### py2exe
```
$ python setup_customized.py
```

### PyInstaller
```
$ pyinstaller main.spec
```

### cx_Freeze
```
$ python setup_cx_Freeze.py build
```

## comparison
||py2exe|PyInstaller|cx_Freeze|
|:-:|:-:|:-:|:-:|
|version|0.6.9|3.3.dev0+483c819|4.3.4|
|file size[MB]|43.5|81.5|44.7|
|execution time[sec]|15|49|8|
|startup time[sec]]|1|5|1|

