from tkinter import *
from tkinter import messagebox

window=Tk()
window.eval('tk::PlaceWindow %s center' %window.winfo_toplevel())
#window.withdraw()

messagebox.showinfo('Aufpassen', 'fehlermeldung', icon='error')
       
 
     
window.deiconify()
window.destroy()
window.quit()
