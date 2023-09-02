import math as mt


def get_hypotenuse(side1, side2):
    hypotenuse = mt.sqrt((side1 * side1) + (side2 * side2))
    return hypotenuse


def create_sequence_list(begin, end):
    sequence_list = []
    for value in range(begin, end):
        sequence_list.append(value)
    return sequence_list


def add_value_list(my_list, value):
    new_list = []
    for list_element in my_list:
        new_list.append(list_element * value)
    return new_list


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
