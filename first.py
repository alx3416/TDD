import numpy as np
from PIL import Image

my_array = np.zeros((255, 255), dtype=np.uint8)
rows, cols = my_array.shape
my_vector = np.linspace(-10, 10, num=255)
my_vector = (np.sin(my_vector) + 1) * 127
for row in range(rows):
    my_array[row, :] = my_vector
my_array2 = my_array.transpose()
my_vector = np.linspace(-5, 5, num=255)
my_vector = (np.sin(my_vector) + 1) * 127
my_array3 = my_array
for row in range(rows):
    my_array3[row, :] = my_vector
my_arrayRGB = np.zeros((255,255,3), dtype=np.uint8)
my_arrayRGB[:, :, 0] = my_array3
my_arrayRGB[:, :, 1] = my_array2
my_arrayRGB[:, :, 2] = my_array
my_image = Image.fromarray(my_arrayRGB)
my_image.show()
