import re
from numpy import matmul

from entities.solution import Step
from calculator_utils.row_echelon import reduced_row_echelon
from calculator_utils.matrix_utils import add_row, validate_matrix
from calculator_utils.string_conversion import str_to_matrix
from calculator_utils.types import Matrix


def calculate_matmul(mat1: Matrix, mat2: Matrix) -> str:
    """Calculates the matrix multiplication of two matrices.

    Args:
        mat1 (Matrix): First matrix as a 2d list.
        mat2 (Matrix): Second matrix as a 2d list.

    Raises:
        ValueError: If matrix multiplication cannot be performed on
        the matrices, i.e. matrices 1 and 2 are not of sizes (k,m)
        and (m,n) respectively.

    Returns:
        Matrix: The resulting matrix as a 2d list.
    """
    validate_matrix(mat1)
    validate_matrix(mat1)

    if len(mat1) != len(mat2[0]):
        raise ValueError("Multiplied matrices must be "
                         "of sizes [k,m] and [m,n]")

    result = matmul(mat1, mat2)
    as_list = []
    for row in result:
        as_list.append(list(row))
    return str(as_list)


def calculate_matsum(mat1: str, mat2: str) -> str:
    """Calculates the element-wise summation of two matrices.

    Args:
        mat1 (Matrix): First matrix as a 2d list.
        mat2 (Matrix): Second matrix as a 2d list.

    Raises:
        ValueError: If matrix summation cannot be performed on
        the matrices, i.e. matrices 1 and 2 are not the same size.

    Returns:
        Matrix: The resulting matrix as a 2d list.
    """
    validate_matrix(mat1)
    validate_matrix(mat2)

    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must be of same size.")

    return str([add_row(row1, mat2[i]) for i, row1 in enumerate(mat1)])


def calculate_matsub(mat1: Matrix, mat2: Matrix) -> Matrix:
    """Calculates the element-wise subtraction of two matrices.

    Args:
        mat1 (Matrix): First matrix as a 2d list.
        mat2 (Matrix): Second matrix as a 2d list.

    Raises:
        ValueError: If matrix subtraciton cannot be performed on
        the matrices, i.e. matrices 1 and 2 are not the same size.

    Returns:
        Matrix: The resulting matrix as a 2d list.
    """
    validate_matrix(mat1)
    validate_matrix(mat2)

    return str([add_row(row1, mat2[i], -1) for i, row1 in enumerate(mat1)])


class CalculatorService:
    """High-level class which UI utilizes to perform calculations."""

    def row_reduce(self, expression: str) -> tuple[str, str]:
        """Calculates the row reduces matrix from given expression if it is valid.

        Args:
            expression (str): String representation of a matrix.

        Returns:
            tuple[str, str]: Tuple of the resulting matrix as as string and
            a string describing the steps to solve.
        """
        expression = str_to_matrix(expression)
        steps: list[Step] = []
        result = reduced_row_echelon(expression, steps)
        steps_str = "\n".join([f"{s.description}\n{s.state}\n" for s in steps])
        return str(result), steps_str

    def matrix_calc(self, expression: str) -> str:
        """Calculates the resulting matrix from given math expression.

        Args:
            expression (str): The string expression of the
            matrix calculation to perform. Summation (+), subtraction (-)
            and matrix multiplication (*) are supported.

        Raises:
            ValueError: If invalid syntax used.

        Returns:
            str: The resulting matrix as a string.
        """
        matrix_pattern = r"(?<=\])\s+[\+\-\*]\s+(?=\[)"
        operator_pattern = r"\]\s+([\+\-\*])\s+\["
        mat_strs = re.split(matrix_pattern, expression)
        operators = re.findall(operator_pattern, expression)

        while len(mat_strs) >= 2 and len(operators) >= 1:
            mat1, mat2 = (str_to_matrix(mat_strs.pop(0)),
                          str_to_matrix(mat_strs.pop(0)))
            operator = operators.pop(0)

            if operator == "+":
                result = calculate_matsum(mat1, mat2)
            elif operator == "-":
                result = calculate_matsub(mat1, mat2)
            elif operator == "*":
                result = calculate_matmul(mat1, mat2)
            else:
                raise ValueError(f"Invalid operator '{operator}'")

            mat_strs.insert(0, result)

        return mat_strs[0].strip()
