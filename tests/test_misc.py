from unittest import TestCase
import utils.misc as ut


class Test(TestCase):
    def test_get_hypotenuse(self):
        result = ut.get_hypotenuse(3, 4)
        self.assertAlmostEqual(5, result, 2)


class TestGeometricShape(TestCase):
    def test_get_area(self):
        shape = ut.GeometricShape(2, 4)
        self.assertEqual(0, shape.get_area())

    def test_get_perimeter(self):
        shape = ut.GeometricShape(2, 4)
        self.assertEqual(8, shape.get_perimeter())


class TestCircle(TestCase):
    def test_get_area(self):
        shape = ut.Circle(5)
        self.assertAlmostEqual(78.539, shape.get_area(), 2)

    def test_get_perimeter(self):
        shape = ut.Circle(3)
        self.assertAlmostEqual(18.849, shape.get_perimeter(), 2)
