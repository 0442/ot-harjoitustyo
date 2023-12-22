import unittest

from calculator_utils.row_echelon import *


class TestEchelon(unittest.TestCase):
    def setUp(self):
        self.I4 = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

    def test_reduced_row_echelon_with_identity_matrix_answers(self):
        m = [
            [1,  2, -1, -4],
            [3,  1, -2,  1],
            [0, -1,  2,  2],
            [1,  0,  3,  2]
        ]
        result = reduced_row_echelon(m)
        self.assertEqual(result, self.I4)

    def test_reduced_row_echelon_with_non_identity_matrix_answers(self):
        m = [
            [1, 3, -1],
            [0, 1,  7],
        ]
        answer = [
            [1, 0, -22],
            [0, 1, 7]
        ]
        result = reduced_row_echelon(m)
        self.assertEqual(result, answer)

    def test_reduced_row_echelon_with_ratnum_answers(self):
        m = [
            [3, 1, 2],
            [1, 2, 3]
        ]
        answer = [
            [1, 0, Rn(1, 5)],
            [0, 1, Rn(7, 5)]
        ]
        result = reduced_row_echelon(m)
        self.assertEqual(result, answer)

    def test_reduced_row_echelon_with_ratnum_matrix_input(self):
        m = [
            [Rn(4, 3), Rn(3, 4), Rn(2, 5)],
            [Rn(5, 2), Rn(4, 3), Rn(3, 4)],
        ]
        answer = [
            [1, 0, Rn(3, 10)],
            [0, 1,        0]
        ]
        result = reduced_row_echelon(m)
        self.assertEqual(result, answer)
