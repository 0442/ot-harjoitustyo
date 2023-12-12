import unittest

from services.calculator_service import CalculatorService


class TestCalculatorService(unittest.TestCase):
    def setUp(self) -> None:
        self._calc = CalculatorService()

    def test_row_reduction_with_valid_syntax(self):
        result = self._calc.row_reduce("[[1/2, 3, 2], [4, 3, 2]]")
        correct = "[[1, 0, 0], [0, 1, 2/3]]"
        self.assertEqual(result, correct)


    def test_row_reduction_with_invalid_syntax(self):
        self.assertRaises(
            ValueError,
            lambda: self._calc.row_reduce("[1/2, 3, 2], 4, 3, 2]")
        )
        self.assertRaises(
            ValueError,
            lambda: self._calc.row_reduce("[1/2, 3, 2], (4, 3, 2)")
        )

    def test_non_symmetric_matrix(self):
        self.assertRaises(
            ValueError,
            lambda: self._calc.row_reduce("[1/2, 3, 2], [4, 3]")
        )