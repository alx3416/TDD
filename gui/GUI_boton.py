# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:54:57 2020

@author: Alejandro
"""

import tkinter as tk

window = tk.Tk()

button = tk.Button(
    text="Click me!",
    width=20,
    height=8,
    bg="black",
    fg="yellow",
).pack()


window.mainloop()