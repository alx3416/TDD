# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:05:14 2019

@author: alx34
"""
from tkinter import *
from tkinter import filedialog
import tkinter as tkr
from PIL import Image
from PIL import ImageTk
import cv2
 
def select_image():
	# referencia paneles globales
	global panelA, panelB
 
	# Abre cuadro de diálogo para seleccionar imagen
	path = filedialog.askopenfilename()
    	# verificar que path hay asea sido seleccionado
	if len(path) > 0:
		# imagen a grises y detectamos bordes
		image = cv2.imread(path)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		edged = cv2.Canny(gray, 50, 100)
 
		# Cambio de BGR a RGB
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# Convertimos a formato para motrar en GUI
		image = Image.fromarray(image)
		edged = Image.fromarray(edged)
 
		# mostramos con Tkinter en lugar de matplotlib
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)
        # si no hay paneles, iniciarlos
		if panelA is None or panelB is None:
			# primer panel guardará imagen seleccionada
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			# segunda imagen guardará bordes
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)
 
		# otro caso, actualiza paneles
		else:
			# actualizar paneles
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged
            # initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Seleccionar imagen", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
# kick off the GUI
root.mainloop()