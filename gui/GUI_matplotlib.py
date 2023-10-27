# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:49:59 2020

@author: alx34
"""

from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Adding Legends")
        self.minsize(640, 400)
        
 
 
        self.matplotCanvas()
 
 
 
 
    def matplotCanvas(self):
        fig = Figure(figsize=(12, 5), facecolor='white')
        axis = fig.add_subplot(111)
        xValues = [1, 2, 3, 4]
        yValues0 = [6, 7.5, 8, 7.5]
        yValues1 = [5.5, 6.5, 8, 6]
        yValues2 = [6.5, 7, 8, 7]
        t0, = axis.plot(xValues, yValues0)
        t1, = axis.plot(xValues, yValues1)
        t2, = axis.plot(xValues, yValues2)
        axis.set_ylabel('Vertical Label')
        axis.set_xlabel('Horizontal Label')
        axis.grid()
        fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third Line '), 'upper right')
 
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
#        toolbar = NavigationToolbar2TkAgg(canvas, self)
#        toolbar.update()
#        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self) #Barra de herramientas de matplotlib
        toolbar.update() # actualizar al haber cambios
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1) # Posicion de toolbar
 
 
 
 
root = Root()
root.mainloop()