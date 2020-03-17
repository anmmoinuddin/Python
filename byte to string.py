#! /usr/bin/python3
import subprocess
p = subprocess.Popen(["ip", "addr"], stdout=subprocess.PIPE)
out, err = p.communicate()

print(out.decode('ascii'))
