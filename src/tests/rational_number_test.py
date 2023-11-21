import unittest

from matrix.rational_number import R

class TestRatNum(unittest.TestCase):
    def setUp(self):
        self.a = R(12, 34)
        self.b = R(56, 78)

    def test_addition_of_rational_nums(self):
        c = self.a + self.b
        self.assertEqual(c, R(710,663))

    def test_subtraction_of_rational_nums(self):
        c = self.a - self.b
        self.assertEqual(c, R(-242,663))

    def test_multiplication_of_rational_nums(self):
        c = self.a * self.b
        self.assertEqual(c, R(56,221))

    def test_division_of_rational_nums(self):
        c = self.a / self.b
        self.assertEqual(c, R(117,238))



    def test_addition_of_ints(self):
        ...
    def test_subtraction_of_ints(self):
        ...
    ...



    def test_reduction_by_scaling_down(self):
        self.assertEqual(R(500,100), 5)
        self.assertEqual(R(5,20), R(1,4))

    def test_reduction_of_negative_divided_by_negative(self):
        self.assertEqual(R(-5,-1), 5)
        self.assertEqual(R(-12,-34), R(12,34))