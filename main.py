import utils.misc as ut


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    foo = ut.get_hypotenuse(3, 4)
    print(foo)

    my_list = ut.create_sequence_list(0, 10)
    new_list = ut.add_value_list(my_list, 4)
    print(my_list)
    print(new_list)

    figure = ut.GeometricShape(3, 5)
    print("número de lados de figura es: ", figure.sides)
    print("perímetro de figura es: ", figure.get_perimeter())
    circle = ut.Circle(7)
    print("nombre de subfigura: ", circle.get_name())
    print("área de círculo: ", circle.get_area())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
