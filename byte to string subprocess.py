#! /usr/bin/python3
from tkinter import *
import subprocess
p = subprocess.Popen(["ip", "addr"], stdout=subprocess.PIPE)
out, err = p.communicate()

print(out.decode('ascii'))

root=Tk()
text=Text(root)
text.pack()
text.insert(END,out.decode('ascii'))
root.mainloop()