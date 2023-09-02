import unittest
import utils.misc as ut


class MyTestCase(unittest.TestCase):
    def test_getHypotenuse(self):
        result = ut.get_hypotenuse(3, 4)
        self.assertEqual(5, result)

    def test_getHypotenuseNegatives(self):
        result = ut.get_hypotenuse(-3, -4)
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()
