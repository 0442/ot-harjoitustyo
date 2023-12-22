import unittest

from calculator_utils.rational_number import Rn


class TestRatNumWithInts(unittest.TestCase):
    def setUp(self):
        self.a = Rn(12, 34)
        self.b = 567

    def test_addition_with_ints(self):
        c = self.a + self.b
        self.assertEqual(c, Rn(19290, 34))

    def test_subtraction_with_ints(self):
        c = self.a - self.b
        self.assertEqual(c, Rn(-19266, 34))

    def test_multiplication_with_ints(self):
        c = self.a * self.b
        self.assertEqual(c, Rn(6804, 34))

    def test_division_with_ints(self):
        c = self.a / self.b
        self.assertEqual(c, Rn(12, 19278))

    def test_comparison_with_ints(self):
        a = Rn(123456789, 123456788)
        b = -1234

        self.assertTrue(a != b)
        self.assertTrue(a > b)
        self.assertFalse(a < b)

        self.assertEqual(Rn(-5, -1), 5)
        self.assertEqual(Rn(-0, -1), 0)


class TestRatNum(unittest.TestCase):
    def setUp(self):
        self.a = Rn(12, 34)
        self.b = Rn(56, 78)

    def test_addition_of_rational_nums(self):
        c = self.a + self.b
        self.assertEqual(c, Rn(710, 663))

    def test_subtraction_of_rational_nums(self):
        c = self.a - self.b
        self.assertEqual(c, Rn(-242, 663))

    def test_multiplication_of_rational_nums(self):
        c = self.a * self.b
        self.assertEqual(c, Rn(56, 221))

    def test_division_of_rational_nums(self):
        c = self.a / self.b
        self.assertEqual(c, Rn(117, 238))

    def test_reduction_by_scaling_down(self):
        self.assertEqual(Rn(500, 100), 5)
        self.assertEqual(Rn(5, 20), Rn(1, 4))

    def test_reduction_of_negative_divided_by_negative(self):
        self.assertEqual(Rn(-12, -34), Rn(12, 34))
        self.assertEqual(Rn(-0, -1), Rn(0, 5))

    def test_reduction_of_zero_nominator(self):
        self.assertEqual(Rn(0, 112312), 0)
        self.assertEqual(Rn(0, 112312), Rn(0, 1))
        self.assertEqual(Rn(0, 112312), Rn(0, -1))

    def test_comparison_with_rational_nums(self):
        digits = 100
        a = Rn(int((digits-1)*"3"+"2"), int(digits*"3"))
        b = Rn(int((digits-1)*"3"+"4"), int(digits*"3"))

        self.assertTrue(a != b)
        self.assertTrue(a < b)
        self.assertFalse(a > b)

        self.assertTrue(a <= b)
        self.assertFalse(a >= b)

        b = a
        self.assertTrue(a >= b)
        self.assertTrue(a <= b)
