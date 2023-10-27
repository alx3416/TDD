# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:01:43 2019

@author: alx34
"""

import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np


class App:
    
    def orig_image(self,event): # event es el identificador para saber que botón activa la función
        btn = event.widget 
        elemento=btn.cget("text")
        
        if elemento=="Original":
            print(elemento)
            self.texto.set("Original")
            self.cv_img = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
            dim = (self.width, self.height)
            self.cv_img = cv2.resize(self.cv_img, dim, interpolation = cv2.INTER_AREA)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        else: # El caso 2 es Original2, en caso de agregar tercer botón, se añade otro if
            print(elemento)
            self.texto.set("Original")
            self.cv_img2 = cv2.cvtColor(cv2.imread(self.image_path2), cv2.COLOR_BGR2RGB)
            dim = (self.width2, self.height2)
            self.cv_img2 = cv2.resize(self.cv_img2, dim, interpolation = cv2.INTER_AREA)
            self.photo2 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img2))
            self.canvas2.create_image(0, 0, image=self.photo2, anchor=tkinter.NW)
    def blur_image(self,event):
        btn = event.widget 
        elemento=btn.cget("text")
        if elemento=="Blur":
            self.texto.set("Blurring")
            p=self.slider1.get()
            self.cv_img = cv2.blur(self.cv_img, (p, p))
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        else:
            self.texto.set("Blurring")
            p=self.slider2.get()
            self.cv_img2 = cv2.blur(self.cv_img2, (p, p))
            self.photo2 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img2))
            self.canvas2.create_image(0, 0, image=self.photo2, anchor=tkinter.NW)
            
    def edge_image(self):
        self.texto.set("Bordes")
        self.cv_img = cv2.Canny(self.cv_img, 75, 150)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
    def kmeans_image(self):
        self.texto.set("K-means")
        img = self.cv_img
        Z = img.reshape((-1,3))
        Z = np.float32(Z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = self.clusters.get()
        ret,label,center=cv2.kmeans(Z,int(K),None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        self.cv_img = res.reshape(self.cv_img.shape)        
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
    def file_image(self):
        # Abre cuadro de diálogo para seleccionar imagen
        image_path = filedialog.askopenfilename()
    	# verificar que path hay asea sido seleccionado
        if len(image_path) > 0:
		# imagen a grises y detectamos bordes
            self.image_path = image_path
            self.cv_img = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
            dim = (self.width, self.height)
            self.cv_img = cv2.resize(self.cv_img, dim, interpolation = cv2.INTER_AREA)
            self.height, self.width, no_channels = self.cv_img.shape
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            
    def orig_imagev(self):
        self.proc = 1
        
    def edge_imagev(self):
        self.proc = 2
            
    def update(self): #Recordemos que es para camara 1, tab 2
        # toma nuevo frame de webcam
        ret, frame = self.vid.get_frame()

        if ret:
            if self.proc == 1: # Caso original
                self.texto2.set("Original")
                self.photo2 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            elif self.proc == 2: #Caso bordes
                self.texto2.set("Bordes")
                frame = cv2.Canny(frame, 75, 150)
                self.photo2 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            else:
                self.photo2 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            
            
            
        self.canvas2.create_image(0, 0, image = self.photo2, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)
            

    
    def __init__(self, window, window_title, image_path="C:\imgs\lena.jpg", video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        #Activamos webcam
        self.vid = MyVideoCapture(self.video_source)
        
        # configuring size of the window 
        self.window.geometry('900x700')
        #Create Tab Control
        self.TAB_CONTROL = ttk.Notebook(window)
        #Tab1
        self.TAB1 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB1, text='Pestaña 1')
        #Tab2
        self.TAB2 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB2, text='Pestaña 2')
        self.TAB_CONTROL.pack(expand=1, fill="both")
        #Tab Name Labels
        self.texto = StringVar()
        self.texto2 = StringVar()
        self.label1 = tkinter.Label(self.TAB1, textvariable=self.texto).grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
        self.label2 = tkinter.Label(self.TAB2, textvariable=self.texto2).grid(row = 0, column = 0, sticky = W, pady = 2)
        self.texto.set("Original")
        self.texto2.set("Original2")
        
    # Elementos para TAB1
        
        self.image_path = image_path
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, (320,240), interpolation = cv2.INTER_AREA)
        self.height, self.width, no_channels = self.cv_img.shape
        self.canvas = tkinter.Canvas(self.TAB1, width = 320, height = 240)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.canvas.grid(row = 8, column = 1, sticky = W, pady = 2)
        
        # Botón para original
        self.btn_orig=tkinter.Button(self.TAB1, text="Original", width=30)
        self.btn_orig.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
        self.btn_orig.bind("<Button-1>", self.orig_image)
#
        # Botón para blur
        self.btn_blur=tkinter.Button(self.TAB1, text="Blur", width=30)
        self.btn_blur.grid(row = 1, column = 1, sticky = W, padx = 2, pady = 2)
        self.btn_blur.bind("<Button-1>", self.blur_image)

        # Slider para blur (tamaño de ventana)
        self.slider1 = tkinter.Scale(self.TAB1, from_=3, to=19, orient=HORIZONTAL, label="Tamaño ventana")
        self.slider1.set(7)
        self.slider1.grid(row = 2, column = 1, sticky = W)
        
        # Botón para bordes
        self.btn_edge=tkinter.Button(self.TAB1, text="Bordes", width=30, command=self.edge_image)
        self.btn_edge.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 2)
        
        # Botón para kmeans
        self.btn_kmeans=tkinter.Button(self.TAB1, text="Kmeans", width=30, command=self.kmeans_image)
        self.btn_kmeans.grid(row = 3, column = 1, sticky = W, padx = 2, pady = 2)
        
        # listado Combobox para seleccionar valores
        self.clusters = StringVar()
        self.combobox =  ttk.Combobox(self.TAB1, width = 5 , textvariable = self.clusters)
        self.combobox['values'] = (2,3,4,5,6,7,8,9,10)
        self.clusters.set(4)
        self.combobox.grid(row = 4, column = 1, sticky = W)
        
        # Botón para cambiar imagen
        self.btn_file=tkinter.Button(self.TAB1, text="Cargar imagen", width=30, command=self.file_image)
        self.btn_file.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)
        
    # Elementos para TAB2
        
        self.canvas2 = tkinter.Canvas(self.TAB2, width = self.vid.widthv, height = self.vid.heightv)
        self.canvas2.grid(row = 1, column = 1, sticky = W, pady = 2)
        
        # Botón para original
        self.btn_origv=tkinter.Button(self.TAB2, text="Original", width=128, command=self.orig_imagev)
        self.btn_origv.grid(row = 2, column = 1, sticky = W, pady = 2)
        
        # Botón para bordes
        icon5=PIL.ImageTk.PhotoImage(file="edges.png")
        self.btn_edgev=tkinter.Button(self.TAB2, image=icon5, width=64, command=self.edge_imagev)
        self.btn_edgev.grid(row = 2, column = 0, sticky = W, pady = 2)

        self.delay = 1 # en milisegundos
        self.proc = 1
        self.update()
        window.mainloop()
        
class MyVideoCapture:
    def __init__(self, video_source=0):
        # Se prueba fuente de video
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("No fue posible encontrar objeto de video", video_source)

        # Tomamos dimensiones de video
        self.widthv = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.heightv = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Si existe captura de webcam, convierte de BGR a RGB
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Al cerrar la ventana debe desactivar la webcam
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Crea ventana y pasa los parámetros para su creación
App(tkinter.Tk(), "Tkinter widgets y OpenCV")