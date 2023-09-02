x = 2
if x == 1:
    print("x = 1")
elif x == 2:
    print("x = 1")
else:
    print("x otro valor")

for i in range(-2, 10, 3):
    print(i)


def sumarvalores(x, y):
    res = x + y
    return res, x, y


print(sumarvalores(2, 2,))


class MiClase():
    def __init__(self):
        self.x = 0


