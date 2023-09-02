import numpy as np
import math as mt

# write the required operations inside each function


def add_2_numbers(x, y):
    # my operations
    result = x + y
    return result


def sum_values_vector(vector):
    # my operations
    result = 0
    for value in vector:
        result = result + value
    return result


def get_max(vector):
    return max(vector)


def get_linear_increment_decrement_vector(min_value, max_value):
    vector1 = range(min_value, max_value + 1)
    vector2 = range(max_value - 1, min_value - 1, -1)
    vector = list(vector1) + list(vector2)
    return vector
