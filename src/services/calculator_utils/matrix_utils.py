from typing import TypeAlias, NamedTuple

from services.calculator_utils.rational_number import Rn


Num: TypeAlias = Rn | int | float
Matrix: TypeAlias = list[list[Rn | int | float]]
RowVector: TypeAlias = list[Rn | int | float]


class SolutionStep(NamedTuple):
    """Represents a step in the process of solving or calculating.

    Attributes:
        description (str): A description of the step.
        state (Matrix): The current state of the calculation.
    """

    description: str
    state: Matrix


Step: TypeAlias = SolutionStep


def add_row(row1: RowVector, row2: RowVector, scalar: Num = 1) -> RowVector:
    """Returns row1 + (scalar * row2).

    Args:
        row1 (RowVector): The first row vector.
        row2 (RowVector): The second row vector.
        scalar (Num): The scalar multiplier (default is 1).

    Returns:
        RowVector: The resulting row vector.

    Raises:
        ValueError: If row vectors are of different lengths.
    """

    if len(row1) != len(row2):
        raise ValueError("Row vectors must be of same length.")

    result_vector = [elem1 + elem2 * scalar for elem1, elem2 in zip(row1, row2)]
    return result_vector


def subtract_row(row1: RowVector, row2: RowVector, scalar: Rn = 1) -> RowVector:
    """Returns row1 - (scalar * row2).

    Args:
        row1 (RowVector): The first row vector.
        row2 (RowVector): The second row vector.
        scalar (Num): The scalar multiplier (default is 1).

    Returns:
        RowVector: The resulting row vector.

    Raises:
        ValueError: If row vectors are of different lengths.
    """
    return add_row(row1, row2, -scalar)


def multiply_row(row: RowVector, scalar: Rn) -> RowVector:
    """Returns a new row where each element is multiplied by the scalar.

    Args:
        row (List[Num]): The row to be multiplied.
        scalar (Num): The scalar multiplier.

    Returns:
        RowVector: The resulting row vector.
    """

    return [element * scalar for element in row]


def arrange_matrix(matrix: Matrix, reverse: bool = False) -> Matrix:
    """Arranges rows in matrices to by leading consecutive zeros.

    Args:
        matrix (Matrix): The matrix to be arranged.
        reverse (bool): If True, arranges in descending order (default is False).

    Returns:
        Matrix: The arranged matrix.
    """

    def leading_zeros(row: RowVector):
        col_i = 0
        count = 0
        while col_i < len(row) and row[col_i] == 0:
            count += 1
            col_i += 1
        return count

    result_matrix = sorted(matrix, key=leading_zeros, reverse=reverse)

    return result_matrix


def leading_num_to_one(row: RowVector) -> RowVector:
    """Returns a new row vector by multiplying it to make the leading number 1.

    Args:
        row (RowVector): The row to be transformed.

    Returns:
        RowVector: The resulting row.
    """
    new_row = row[:]

    for elem in row:
        if elem != 0:
            new_row = multiply_row(row, Rn(1, elem))
            break

    return new_row


def all_leading_nums_to_one(matrix: Matrix, steps: list[Step]) -> Matrix:
    """Multiply each row of a matrix to make the leading numbers 1.

    Args:
        matrix (Matrix): The matrix to be transformed.
        steps (List[Step]): The list to append steps to (modified in place).

    Returns:
        Matrix: The resulting matrix.
    """
    result = matrix[:]

    for row_i, row in enumerate(matrix):
        n_row = leading_num_to_one(row)
        if n_row != row:
            desc = f"Turn the leading number to 1 by multiplying R_{row_i+1}"
            steps.append(Step(desc, result[:]))
        result[row_i] = n_row

    return result


def first_non_zero(vector: RowVector) -> int:
    """Finds the index of the first non-zero number in a list.

    Returns:
        int: The index of the first non-zero number or None if all numbers are zeros.
    """
    for i, num in enumerate(vector):
        if num != 0:
            return i
    return None


def validate_matrix(matrix: Matrix):
    width = len(matrix[0])

    for row in matrix:
        if len(row) != width:
            raise ValueError("All rows must have the same length.")
