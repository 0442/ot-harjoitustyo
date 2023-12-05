from typing import TypeAlias, NamedTuple

from calculator.utils.rational_number import Rn


class SolutionStep(NamedTuple):
    """Represents a step in the process of solving / calculating"""
    description: str
    state: list[list[Rn]]


Step: TypeAlias = SolutionStep


def add_row(row1: list[Rn], row2: list[Rn], scalar: Rn | int) -> list[int]:
    """Returns row + (scalar * row2).

    row2 is multiplied by scalar and added to row1 and the resulting
    vector is returned.

    Rows are lists of rational numbers. Scalar is an integer.

    Rows must be the same length, otherwise an ValueError is raised.
    """
    if len(row1) != len(row2):
        raise ValueError("Row vectors must be of same length.")

    result_vector = []
    col_count = len(row1)

    for col_i in range(col_count):
        result_vector.append(row1[col_i] + row2[col_i] * scalar)

    return result_vector


def subtract_row(row1: list[int], row2: list[int], scalar: Rn | int) -> list[int]:
    """
    Same as calling add_row with a scalar*(-1).
    Refer to add_row for documentation.
    """
    return add_row(row1, row2, -scalar)


def multiply_row(row: list[Rn | int], scalar: Rn | int):
    new_row = []
    for element in row:
        new_row.append(element * scalar)
    return new_row


def arrange_matrix(matrix: list[list[Rn]], reverse: bool = False) -> list[list[Rn]]:
    """
    Arranges rows in matrices so that the least amount of leading
    consecutive zeros are at the top and the most leading
    consecutive zeros are at the bottom.
    """

    def leading_zeros(row: list[Rn]):
        col_i = 0
        count = 0
        while col_i < len(row) and row[col_i] == 0:
            count += 1
            col_i += 1
        return count

    result_matrix = sorted(matrix, key=leading_zeros, reverse=reverse)

    return result_matrix


def leading_num_to_one(row: list[Rn]):
    new_row = row[:]

    for elem in row:
        if elem != 0:
            new_row = multiply_row(row, Rn(1, elem))
            break

    return new_row


def all_leading_nums_to_one(matrix: list[list[Rn]], steps: list[Step]):
    """Multiply each row of a matrix so that the leading numbers
    of each row becomes 1."""
    result = matrix[:]

    for row_i, row in enumerate(matrix):
        n_row = leading_num_to_one(row)
        if n_row != row:
            desc = f"Turn the leading number to 1 by multiplying R_{row_i+1}"
            steps.append(Step(desc, result[:]))
        result[row_i] = n_row

    return result


def first_non_zero(vector: list[Rn]):
    """Finds the index of the first non-zero number in list
    Returns None if all numbers are zeros.
    """
    for i, num in enumerate(vector):
        if num != 0:
            return i
    return None


def validate_matrix(matrix: list[list[Rn]]):
    width = len(matrix[0])

    for row in matrix:
        if len(row) != width:
            raise ValueError
