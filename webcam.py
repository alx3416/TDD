import cv2
import numpy as np
import mylibrary as mylib


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        rows, cols, chan = img.shape
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apliquemos transformaciones de intensidad (operaciones aritméticas)
        Im1neg = cv2.bitwise_not(img_gray)
        # gradiente horizontal
        img_gradiente = mylib.gradiente_horizontal(img_gray)

        cv2.imshow('my webcam', img_gradiente)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


show_webcam()
