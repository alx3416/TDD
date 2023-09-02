from unittest import TestCase
import utils.ramp_on as ro


class Test(TestCase):
    def test_add_2_numbers(self):
        result = ro.add_2_numbers(2, 2)
        self.assertAlmostEqual(4, result, 2)

    def test_sum_values_vector(self):
        result = ro.sum_values_vector([1, 2, 3, 4, 5])
        self.assertEqual(15, result)

    def test_get_max(self):
        result = ro.get_max([1, 2, 3, 4, 5])
        self.assertEqual(5, result)

    def test_get_linear_increment_decrement_vector(self):
        result = ro.get_linear_increment_decrement_vector(-3, 3)
        self.assertEqual([-3, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3], result)
