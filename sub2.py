#! /usr/bin/python3.7

import subprocess


#shell=True,
proc1=subprocess.Popen("/home/pi/Desktop/getip.py",  stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = proc1.communicate()
print(out)

