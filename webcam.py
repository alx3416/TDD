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
        # img_filtrado = mylib.filtrado_local(img_gray)
        kernel = np.ones((7, 7), np.float32) / 49
        img_filtrado = cv2.filter2D(img_gray, -1, kernel)
        kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], np.float32)
        img_filtrado = cv2.filter2D(img_filtrado, -1, kernel)

        cv2.imshow('my webcam', img_filtrado)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


show_webcam()
