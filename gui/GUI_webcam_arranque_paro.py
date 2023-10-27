# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:59:23 2019

@author: alx34
"""
from tkinter import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import numpy as np
from LBP import LBP
# Clase principal que contendrá todos los llamados
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Activa webcam
        self.vid = MyVideoCapture(self.video_source)

        # tomamos características de frame para construir panel
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # Botón para guardar snapshots
        self.btn_snapshot=tkinter.Button(window, text="Arranque", width=128, command=self.arranque)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        
        # Botón para original
        self.btn_orig=tkinter.Button(window, text="Paro", width=128, command=self.paro)
        self.btn_orig.pack(anchor=tkinter.CENTER, expand=False)
        
        # Botón para bordes
        icon5=PIL.ImageTk.PhotoImage(file="edges.png")
        self.btn_edge=tkinter.Button(window, image=icon5, width=64, command=self.edge_image)
        self.btn_edge.pack(side = LEFT)
        
        # Botón para blurring
        icon1=PIL.ImageTk.PhotoImage(file="blur.png")
        self.btn_blur=tkinter.Button(window, image=icon1, width=64, command=self.blur_image)
#        self.btn_blur.pack(anchor=tkinter.W, expand=True)
        self.btn_blur.pack(side = LEFT)
        # Botón para Hough rectas
        icon2=PIL.ImageTk.PhotoImage(file="lines.png")
        self.btn_lines=tkinter.Button(window, image=icon2, width=64, command=self.lines_image)
        self.btn_lines.pack(side = LEFT)
        
        # Botón para Hough rectas
        icon3=PIL.ImageTk.PhotoImage(file="laplacian.png")
        self.btn_grad=tkinter.Button(window, image=icon3, width=64, command=self.grad_image)
        self.btn_grad.pack(side = LEFT)
        
        # Botón para LBP
        icon4=PIL.ImageTk.PhotoImage(file="LBP.png")
        self.btn_LBP=tkinter.Button(window, image=icon4, width=64, command=self.LBP_image)
        self.btn_LBP.pack(side = LEFT)
        
        # Botón para circulos
        icon6=PIL.ImageTk.PhotoImage(file="circles.png")
        self.btn_circles=tkinter.Button(window, image=icon6, width=64, command=self.circles_image)
        self.btn_circles.pack(side = LEFT)

        # Después de ser llamado 1 ves, el método esperará un delay y repetirá el proceso
        self.delay = 1 # en milisegundos
        self.proc = 10
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.img1 = cv2.imread('C:/imgs/controller.png',0) 
        
        self.update()

        self.window.mainloop()

    def arranque(self):
        # Callback para botón de snapshot
        self.proc = 0
    
    def paro(self):
        self.proc = 1
        
    def edge_image(self):
        self.proc = 2
        
    def blur_image(self):
        self.proc = 3
    
    def lines_image(self):
        self.proc = 4
        
    def grad_image(self):
        self.proc = 5
        
    def LBP_image(self):
        self.proc = 6
        
    def circles_image(self):
        self.proc = 7

    def update(self):
        # toma nuevo frame de webcam
        ret, frame = self.vid.get_frame()
        # Siempre detectando aqui va el codigo para deteccion
        
        
        kp1, des1 = self.sift.detectAndCompute(self.img1,None)
        kp2, des2 = self.sift.detectAndCompute(frame,None)

    # BFMatcher with default params
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2, k=2)

    # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append([m])
    
        # cv2.drawMatchesKnn expects list of lists as matches.
        img3 = cv2.drawMatchesKnn(self.img1,kp1,frame,kp2,good,None,flags=2)
        if len(good)>6: #si queremos activar un actuador o LED cuando detecte algo
            cv2.putText(frame,'detectado',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,200,0),2)
            #GPIO.output(33, True)
            
        #else : GPIO.output(33, False)
            # End code
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        if ret:
            if self.proc == 0: # Caso Arranque
                #codigo para deteccion
                print("Encender led")
                
                
                
            elif self.proc == 1: # Caso Paro
                print("LED apagado")
                
            elif self.proc == 2: #Caso bordes
                frame = cv2.Canny(frame, 75, 150)
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            elif self.proc == 3:
                frame = cv2.blur(frame, (7, 7))
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            elif self.proc == 4:
                cimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cimg = cv2.medianBlur(cimg,7)
                #    cimg = cv2.bilateralFilter(cimg,11,25,25)
                edges = cv2.Canny(cimg, 75, 150)
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, maxLineGap=50)
                if lines is not None: 
                    for line in lines:
                        x1, y1, x2, y2 = line[0]
                        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            elif self.proc ==5:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.medianBlur(frame,7)
                G = cv2.Laplacian(frame,cv2.CV_64F)
                frame = ((G-G.min())/(G.max()-G.min()))*255
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            elif self.proc == 6:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = LBP(frame, 3)
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            elif self.proc == 7:
                cimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cimg = cv2.medianBlur(cimg,7)
                #    cimg = cv2.bilateralFilter(cimg,11,25,25)
                edges = cv2.Canny(cimg, 75, 150)
                circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,50,
                            param1=80,param2=30,minRadius=30,maxRadius=70)
                if circles is not None:
                    circles = np.uint16(np.around(circles))
                    for i in circles[0,:]:
                        # draw the outer circle
                        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                        # draw the center of the circle
                        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            else:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            
            
            
        self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Se prueba fuente de video
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("No fue posible encontrar objeto de video", video_source)

        # Tomamos dimensiones de video
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

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
App(tkinter.Tk(), "Tkinter y OpenCV")