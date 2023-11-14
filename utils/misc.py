import math as mt


def get_hypotenuse(side1, side2):
    hypotenuse = mt.sqrt((side1 * side1) + (side2 * side2))
    return hypotenuse

# Utiliza map para crear una lista que contenga el doble de cada elemento de otra lista dada

myList = [1, 2, 3, 4]
def duplicate(n):
    return n * 2

result = map(duplicate, myList)
print(list(result))

# Utiliza filter para obtener lista de numeros impares

ages = [2, 8, 17, 31, 22, 32]

def getOdds(x):
  if x % 2 == 0:
    return False
  else:
    return True

nones = filter(getOdds, ages)
print(list(nones))

# Utiliza reduce para la suma acumulativa de una lista de numeros

import functools
numeros = [1, 2, 3, 4, 5]
acumulador = functools.reduce(lambda a, b: a+b, numeros)
print(acumulador)

# Utiliza map para crear lista de longitudes de palabras a partir de lista de palabras

# Utiliza filter para obtener una lista de palabras que tengan mas de cierta longitud de una lista dada

# Utiliza reduce para encontrar el producto de todos los elementos de una lista de numeros

# Utiliza map para convertir todas las palabras de una lista a mayusculas

# Utiliza filter para obtener los numeros primos de una lista

# Abrir un archivo y almacenar en un diccionario como clave, cada palabra del archivo y valor la cantidad de veces que se repite


class GeometricShape:
    def __init__(self, sides, side_length):
        self.perimeter = 0.0
        self.area = 0.0
        self.name = "figure"
        self.sides = sides
        self.side_length = side_length

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area

    def get_perimeter(self):
        self.perimeter = self.side_length * self.sides
        return self.perimeter


class Circle(GeometricShape):
    def __init__(self, radius):
        self.number_sides = 1
        self.radius = radius
        self.name = "circle"

    def get_area(self):
        return mt.pi * (mt.pow(self.radius, 2))

    def get_perimeter(self):
        return mt.pi * (self.radius * 2)
