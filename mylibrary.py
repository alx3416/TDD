import numpy as np


def gamma_correction_one_channel(img, gamma):
    img = np.double(img)  # Conversión tipo de dato
    img = img / 255  # Cambio de rango de 0 a 1
    img = np.power(img, gamma)  # Transformación gamma
    img = img * 255  # Regresamos a rango 0 a 255
    img = np.uint8(img)  # Regresamos a tipo de dato uint8
    return img


def gradiente_horizontal(matriz):
    rows, cols = matriz.shape
    matriz_gradiente = matriz.copy()
    for row in range(rows):
        for col in range(0, cols-1):
            matriz_gradiente[row, col] = matriz[row, col] - matriz[row, col+1]
    matriz_gradiente = np.uint8((matriz_gradiente + 255)/2)
    return matriz_gradiente
