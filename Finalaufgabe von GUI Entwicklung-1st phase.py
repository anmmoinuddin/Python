#json
import json

 
#tkinter library
from   tkinter import *
import tkinter as tk

#pygame library
from pygame import *

#import python Image Library
from PIL import Image, ImageTk

#function declaration

def   quit_app():
      my_window.destroy()

      #button music
def play_music():
    mixer.init()
    mixer.music.load('punch.wav')
    mixer.music.play()


    while mixer.music.get_busy():
          time.Clock().tick(2)
 
      
def open_window():

                

                play_music()

                
                #my_window.withdraw()  
                top=Toplevel()
                top.title('NeuFenster')
                top.geometry("%dx%d+0+0" % (width_value, height_value))
                button_1=Button(top,
                                text="Schließen",
                                font="Times 12",
                                pady=20,
                                padx=20,
                                bg='#40E0D0',
                                command=top.destroy)
                
                 
                button_1.pack()
                 
# Title Window
my_window=Tk()

#Outsourcing Image
photo=PhotoImage(file='C:\\Users\\moin\\PycharmProjects\\untitled1\\deer.png')

 

#creation of menubar/associating menubar with my_window instance
my_menubar=Menu(my_window)

#my_menubar.add_command(label='Menu')
my_dropdown_menu=Menu(my_menubar)
my_dropdown_menu.add_command(label='Start',command=open_window)
my_dropdown_menu.add_command(label='Stop',command=open_window)
my_dropdown_menu.add_command(label='Techno', command=open_window)
my_dropdown_menu.add_command(label='power',command=open_window)
 
my_menubar.add_cascade(label='Menu', menu=my_dropdown_menu)           
my_menubar.add_command(label='Quit', command=quit_app)
my_window.config(menu=my_menubar)


# json file 
Objektliste='''

{
"Objekt":
      [
      {
      "id": 1,
      "posx": 8,
      "posy": 9,
      "width": 200,
      "height":300,
      "textname": "Start",
      "img": "C:/Users/moin/Desktop/pr3/3.png",  
      "color": "blue",
      "beep": "punch.wav",
      "exec": "shutdown.py",
      "answer": 2
      },

      {
      "id": 2,
      "posx": 8,
      "posy": 10,
      "width": 200,
      "height": 300,
      "textname": "Stop",
      "img": "C:/Users/moin/Desktop/pr3/3.png",
      "color": "blue",
      "beep": "punch.wav",
      "exec": "shutdown.py",
      "answer": 2
      },

      {
      "id": 3,
      "posx": 8,
      "posy": 11,
      "width": 200,
      "height": 300,
      "textname": "Techno",
      "img":"C:/Users/moin/Desktop/pr3/4.png",
      "color": "blue",
      "beep": "punch.wav",
      "exec": "shutdown.py",
      "answer": 4
      },

      {
      "id": 4,
      "posx": 8,
      "posy": 12,
      "width": 200,
      "height": 300,
      "textname": "Power",
      "img":  "C:/Users/moin/Desktop/pr3/5.png",
      "color": "blue",
      "beep": "punch.wav",
      "exec": "shutdown.py",
      "answer": 1
      }
      
      ]

}

'''

#Title of the window
my_window.title("Home Automation")
my_window.configure(background='white')

#full window preview/Vorschau
width_value=my_window.winfo_screenwidth()
height_value=my_window.winfo_screenwidth()

#canvas=Canvas(my_window, width=width_value, height=height_value)
#canvas.pack()
#canvas.create_image(0,0,anchor=NW, image=photo)

my_window.geometry("%dx%d+0+0" % (width_value, height_value))

frame1=tk.Frame(my_window)
frame1.pack(side=tk.TOP, fill=tk.X)

#frame2=tk.Frame(my_window)
#frame2.pack(side=tk.TOP, fill=tk.X)

#frame3=tk.Frame(my_window)
#frame3.pack(side=tk.TOP, fill=tk.X)


data=json.loads(Objektliste)
mycontainer=[] 
          
#Creation of for loop/Erzeugt von for loop
for item in data['Objekt']:
            button  = item['id']
            buttonText = item['textname']
            colour=item['color']
            width=item['width']
            height= item['height']
            posx = item['posx']
            posy = item['posy']
            imagePath=item['img']
            cmd  = item['exec']

            
            #Creation of button
              

             
            myImage=PhotoImage(file=imagePath)

            mycontainer.append(myImage)
            
            button = Button( frame1,
                            
                             compound=tk.TOP,
                             fg=colour,
                             width=width,
                             height=height,
                             bg="white",
                            
                             font="Times 32",
                             relief="groove",
                             image=myImage,
                             text=buttonText,
                             pady=20,
                             padx=20,
                             command=open_window)
                            
             
            button.grid(column=posy, row=posx)  

            #print(button['text'])
# end of loop




 
my_window.mainloop()
