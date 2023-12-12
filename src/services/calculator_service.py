from re import sub

from services.calculator_utils.row_echelon import reduced_row_echelon
from services.calculator_utils.rational_number import Rn
from services.calculator_utils.matrix_utils import Matrix, Num


def str_to_num(num_str: str) -> Num:
    """Parses a string representing a number into a number.

    Args:
        num_str (str): A string representing a number.

    Returns:
        Num: The number (float, int, Rn) the string represents.

    Raises:
        ValueError if the format is invalid.
    """
    try:
        if num_str.count("/") == 1:
            rn = num_str.split("/")
            return Rn(int(rn[0]), int(rn[1]))

        if num_str.count(".") == 1:
            return float(num_str)

        return int(num_str)
    except ValueError:
        raise ValueError(f"Invalid number format: {num_str}")


def str_to_matrix(expression: str) -> Matrix:
    """Parses user written matrix expression into a matrix.

    Args:
        expression (str): A string representing a matrix. It can be formed using [], {} or ().

    Returns:
        Matrix: The matrix the expression represents.

    Raises:
        ValueError if the format is invalid.
    """
    expr = sub(r"\ +", r"", expression)
    expr = expr.strip(r"[](){},")

    if expr.count("],[") != 0:
        rows = expr.split(r"],[")
    elif expr.count("},{") != 0:
        rows = expr.split(r"},{")
    elif expr.count("),(") != 0:
        rows = expr.split(r"),(")
    else:
        rows = [expr]

    result = []
    for r in rows:
        nums = r.split(",")
        new_row = []
        for n in nums:
            new_row.append(str_to_num(n))
        result.append(new_row)

    return result


class CalculatorService:
    """High-level class which UI utilizes to perform calculations."""

    def __init__(self) -> None:
        ...

    def row_reduce(self, expression: str) -> str:
        """Calculates the row reduces matrix from given expression if it is valid.

        Args:
            expression (str): _description_

        Returns:
            str: _description_
        """
        expression = str_to_matrix(expression)
        result = reduced_row_echelon(expression, [])
        return str(result)

    def matrix_calc(self, expression: str) -> str:
        ...
