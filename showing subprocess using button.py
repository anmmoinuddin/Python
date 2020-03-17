from tkinter import *
import subprocess

a=Tk()

def mfil():
    proc1=subprocess.Popen("/home/pi/Desktop/getip.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = proc1.communicate()

    print(out)

button=Button(text='open file', width=30, command=mfil).pack()
a.mainloop()