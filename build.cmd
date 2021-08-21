@echo off
pyinstaller -D -w -n PerfectFall -i assets/icon.ico main.py -p Util.py --hidden-import Util
g++ PerfectFall.Cpp/launch.cpp icon.o -m64 -o Launch.exe
copy Launch.exe dist/PerfectFall/
copy Util.py dist/PerfectFall/
copy assets dist/PerfectFall/