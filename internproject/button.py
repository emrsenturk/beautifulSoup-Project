
from tkinter import *
import sys
import os
import tkinter
from tkinter import messagebox


top=tkinter.Tk()
def helloCallBack():
     os.system('python mavi.py')

def defacto():
     os.system('python defacto.py')

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
    
    #Creation of init_window
    def init_window(self):
        
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = tkinter.Button(top,text="Mavi",command= helloCallBack)
        quitButton.pack()
        # placing the button on my window
        quitButton.place(x=10, y=0)

        quitButton2 = tkinter.Button(top,text="Defacto",command= defacto)
        quitButton2.pack()
        # placing the button on my window
        quitButton2.place(x=50, y=0)

#size of the window
top.geometry("400x300")

app = Window(top)
top.mainloop()

