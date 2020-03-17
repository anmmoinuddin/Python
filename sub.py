
#! /usr/bin/python3.7

import subprocess

proc1=subprocess.Popen("/home/pi/Desktop/getlog.py 64 abc", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc1.communicate()
print(out)