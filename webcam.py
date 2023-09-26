import cv2
import numpy as np


def show_webcam():
    cam = cv2.VideoCapture(0)
    count = 0
    while True:
        count = count + 1
        if count >= 255:
            count = 0
        ret_val, img = cam.read()
        rows, cols, chan = img.shape
        img_gray = np.zeros((rows, cols), dtype=np.uint8)
        img_bin = np.zeros((rows, cols), dtype=np.uint8)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        idx = img_gray[:, :] >= count
        img_bin[idx] = 255
        cv2.imshow('my webcam', img_bin)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


show_webcam()
