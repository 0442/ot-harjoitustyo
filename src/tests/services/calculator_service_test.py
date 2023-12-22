import unittest

from services.calculator_service import CalculatorService


class TestCalculatorService(unittest.TestCase):
    def setUp(self) -> None:
        self._calc = CalculatorService()

    def test_row_reduction_with_valid_syntax(self):
        result, solution = self._calc.row_reduce("[[1/2, 3, 2], [4, 3, 2]]")
        correct = "[[1, 0, 0], [0, 1, 2/3]]"
        self.assertEqual(result, correct)
        self.assertIsInstance(solution, str)

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

    def test_matmul_with_valid_syntax(self):
        result = self._calc.matrix_calc(
            "[[1/2, 2, 3], [4, 5/3, 6], [7,8, 9/2]] * [[1,2,3], [4,5,6], [7,8,9]]"
        )
        answer = "[[59/2, 35, 81/2], [158/3, 193/3, 76], [141/2, 90, 219/2]]"
        self.assertEqual(result, answer)

    def test_matsum_with_valid_syntax(self):
        result = self._calc.matrix_calc(
            "[[1/2, 2, 3], [4, 5/3, 6], [7,8, 9/2]] + [[1,2,3], [4,5,6], [7,8,9]]"
        )
        answer = "[[3/2, 4, 6], [8, 20/3, 12], [14, 16, 27/2]]"
        self.assertEqual(result, answer)

    def test_matsub_with_valid_syntax(self):
        result = self._calc.matrix_calc(
            "[[1/2, 2, 3], [4, 5/3 ,6], [7, 8, 9/2]] - [[1,2,3], [4,5,6], [7,8,9]]"
        )
        answer = "[[-1/2, 0, 0], [0, -10/3, 0], [0, 0, -9/2]]"
        self.assertEqual(result, answer)

    def test_matrix_calc_with_invalid_syntax(self):
        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[1,23,] + [1,2,4]")
        )
        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[1,23,] * [1,2,4]")
        )
        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[1,23,] - [1,2,4]")
        )

    def test_matmul_with_invalid_matrices(self):
        # Multiplication
        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[[1,2,3,4]] * [[1,2,3,4]]")
        )

        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[[1], [2], [3]] * [[1,2,3,4]]")
        )

    def test_matsum_with_invalid_matrices(self):
        # Summation
        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[[1,2,3,4]] + [[1,2,3]]")
        )

        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[[1], [2], [3]] + [[1,2,3,4]]")
        )

    def test_matsub_with_invalid_matrices(self):
        # Subtraction
        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[[1,2,3,4]] - [[1,2,3]]")
        )

        self.assertRaises(
            ValueError,
            lambda: self._calc.matrix_calc("[[1], [2], [3]] - [[1,2,3,4]]")
        )
