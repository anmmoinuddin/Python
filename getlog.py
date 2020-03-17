#! /usr/bin/python3.7

import subprocess
p = subprocess.Popen(["tail", "/var/log/bootstrap.log"], stdout=subprocess.PIPE)
out, err = p.communicate()
print(out)