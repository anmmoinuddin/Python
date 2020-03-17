#json
import json
 

 
#tkinter library
from   tkinter import *
import tkinter as tk

#pygame library
from pygame import *

#import python Image Library
from PIL import Image, ImageTk


#importing  json file  

with open("C:\\Users\\moin\\Desktop\\lcars\\lcars.json") as f:
      data=json.load(f)

#functions

def   quit_app():
      my_window.destroy()

#button music
def play_music():
    mixer.init()
    mixer.music.load(data['main'][1]['beep'])
    mixer.music.play()


    while mixer.music.get_busy():
          time.Clock().tick(2)
 
#creating the log windows
def create_window():

                play_music()  
                lwindow = tk.Toplevel()

                  #full window preview/Vorschau
                width_value=lwindow.winfo_screenwidth()
                height_value=lwindow.winfo_screenwidth()

                lwindow.geometry("%dx%d+0+0" % (width_value, height_value))
                button_0=Button(lwindow,
                                text="Schließen",
                                font="Times 12",
                                pady=20,
                                padx=20,
                                bg='#40E0D0'
                              
            
                                
                                )
                button_0.grid(column=data['log'][0]['posy'],row=data['log'][0]['posx'])
                button1 = Button(   lwindow,  
                  
                                    fg='blue',
                                    width=9,
                                    height=4,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text= data['log'][1]['id'],
                                    pady=20,
                                    padx=20
                                    )
                            
             
                button1.grid(column=data['log'][1]['posy'],row=data['log'][1]['posx'])

                button2= Button(   lwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['log'][2]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button2.grid(column=data['log'][2]['posy'],row=data['log'][2]['posx'])

                button3= Button(    lwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['log'][3]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button3.grid(column=data['log'][3]['posy'],row=data['log'][3]['posx'])
                 
                button4= Button(    lwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['log'][4]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button4.grid(column=data['log'][4]['posy'],row=data['log'][4]['posx'])

                button5= Button(    lwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['log'][5]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button5.grid(column=data['log'][5]['posy'],row=data['log'][5]['posx'])
                 
                button6= Button(    lwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['log'][6]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button6.grid(column=data['log'][6]['posy'],row=data['log'][6]['posx'])
#creating the media windows
def media_window():
                mwindow = tk.Toplevel()

                  #full window preview/Vorschau
                width_value=mwindow.winfo_screenwidth()
                height_value=mwindow.winfo_screenwidth()

                mwindow.geometry("%dx%d+0+0" % (width_value, height_value))
                button_0=Button(mwindow,
                                text="Schließen",
                                font="Times 12",
                                pady=20,
                                padx=20,
                                bg='#40E0D0'
                              
            
                                
                                )
                button_0.grid(column=data['media'][0]['posy'],row=data['log'][0]['posx'])
                button1 = Button(   mwindow,  
                  
                                    fg='blue',
                                    width=9,
                                    height=4,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text= data['media'][1]['id'],
                                    pady=20,
                                    padx=20
                                    )
                            
             
                button1.grid(column=data['media'][1]['posy'],row=data['log'][1]['posx'])

                button2= Button(   mwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['media'][2]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button2.grid(column=data['media'][2]['posy'],row=data['log'][2]['posx'])

                button3= Button(    mwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['media'][3]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button3.grid(column=data['media'][3]['posy'],row=data['log'][3]['posx'])
                 
                button4= Button(   mwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['media'][4]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button4.grid(column=data['media'][4]['posy'],row=data['log'][4]['posx'])

                button5= Button(    mwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['media'][5]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button5.grid(column=data['media'][5]['posy'],row=data['log'][5]['posx'])
                 
                button6= Button(    mwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['media'][6]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button6.grid(column=data['media'][6]['posy'],row=data['media'][6]['posx'])
#configuration window                 
def conf_window():
                cwindow = tk.Toplevel()

                  #full window preview/Vorschau
                width_value=cwindow.winfo_screenwidth()
                height_value=cwindow.winfo_screenwidth()

                mwindow.geometry("%dx%d+0+0" % (width_value, height_value))
                button_0=Button(cwindow,
                                text="Schließen",
                                font="Times 12",
                                pady=20,
                                padx=20,
                                bg='#40E0D0'
                              
            
                                
                                )
                button_0.grid(column=data['conf'][0]['posy'],row=data['log'][0]['posx'])
                button1 = Button(   cwindow,  
                  
                                    fg='blue',
                                    width=9,
                                    height=4,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text= data['conf'][1]['id'],
                                    pady=20,
                                    padx=20
                                    )
                            
             
                button1.grid(column=data['conf'][1]['posy'],row=data['conf'][1]['posx'])

                button2= Button(   cwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['conf'][2]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button2.grid(column=data['conf'][2]['posy'],row=data['conf'][2]['posx'])

                button3= Button(    cwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['conf'][3]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button3.grid(column=data['conf'][3]['posy'],row=data['conf'][3]['posx'])
                 
                button4= Button(   cwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['conf'][4]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button4.grid(column=data['conf'][4]['posy'],row=data['conf'][4]['posx'])

                button5= Button(    cwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['conf'][5]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button5.grid(column=data['conf'][5]['posy'],row=data['conf'][5]['posx'])
                 
                button6= Button(    cwindow, 
                  
                                    fg='blue',
                                    width=10,
                                    height=5,
                                    bg='green',                
                                    font="Times 32",
                   
                             #image=myImage,
                                    text=data['conf'][6]['id'],
                                    pady=20,
                                    padx=20)
              
                            
             
                button6.grid(column=data['conf'][6]['posy'],row=data['conf'][6]['posx'])
                                  
#main window
my_window = tk.Tk()
#Title of the window
my_window.title("Home Automation")
my_window.configure(background='white')

#full window preview/Vorschau
width_value=my_window.winfo_screenwidth()
height_value=my_window.winfo_screenwidth()

my_window.geometry("%dx%d+0+0" % (width_value, height_value))

#creation of menubar/associating menubar with my_window instance
my_menubar=Menu(my_window)

#my_menubar.add_command(label='Menu')
my_dropdown_menu=Menu(my_menubar)
my_dropdown_menu.add_command(label='main' )
my_dropdown_menu.add_command(label='log' )
my_dropdown_menu.add_command(label='media' )
my_dropdown_menu.add_command(label='config' )
 
my_menubar.add_cascade(label='Menu', menu=my_dropdown_menu)           
my_menubar.add_command(label='Quit', command=quit_app)
my_window.config(menu=my_menubar)


#background Image

background_image=ImageTk.PhotoImage(Image.open('C:\\Users\\moin\\Desktop\\lcars\\bg1.jpg'))

background_label = tk.Label(my_window, image=background_image)
background_label.place(x=600, y=350)
#canvas = Canvas(my_window, width=width_value, height=height_value)
#canvas.grid()
#canvas.create_image(0,0,anchor=NW, image=background_image)


b = tk.Button(my_window, text="Create new window", command=create_window)
b.grid()

button1 = Button(  
                  
                  fg='blue',
                  width=9,
                  height=4,
                  bg='green',                
                  font="Times 32",
                   
                  #image=PhotoImage(file=data['main'][0]['img']),
                  text= data['main'][1]['id'],
                  pady=20,
                  padx=20
                   
                  )
                            
             
button1.grid(column=data['main'][1]['posy'],row=data['main'][1]['posx'])

button2 = Button(  
                  
                  fg='blue',
                  width=9,
                  height=4,
                  bg='green',                
                  font="Times 32",
                   
                  #image=myImage,
                  text= data['main'][2]['id'],
                  pady=20,
                  padx=20
                   
                  )
                            
             
button2.grid(column=data['main'][2]['posy'],row=data['main'][2]['posx'])

my_window.mainloop()
