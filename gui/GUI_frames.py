# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:10:04 2020

@author: Alejandro
"""

import tkinter as tk

# # Codigo solo ejemplo crear frame vacio
# window = tk.Tk()
# # Un frame es un contenedor de widgets, se ajusta por default al mismo tamaño de la ventana principal
# frame = tk.Frame()
# frame.pack()

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="Estoy en el frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="Estoy en el frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
