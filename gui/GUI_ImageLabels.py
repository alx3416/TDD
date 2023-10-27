# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:43:36 2020

@author: Alejandro
"""

from tkinter import *
from PIL import  Image
from tkinter import filedialog

class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 650, 650
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.pack()

        self.file = Button(self, text='Browse', command=self.choose)
        self.choose = Label(self, text="Choose file").pack()
        self.image = PhotoImage(file='circles.png')
        self.label = Label(image=self.image)


        self.file.pack()
        self.label.pack()

    def choose(self):
        path = filedialog.askopenfilename()
        self.image2 = PhotoImage(file=path)
        self.label.configure(image=self.image2)
        self.label.image=self.image2


root = Tk()
app = GUI(master=root)
app.mainloop()
root.destroy()