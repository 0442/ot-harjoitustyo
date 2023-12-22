import re

from calculator_utils.types import Num, Matrix, Rn


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
    except ValueError as exc:
        raise ValueError(f"Invalid number format: {num_str}") from exc


def str_to_matrix(expression: str) -> Matrix:
    """Parses user written matrix expression into a matrix.

    Args:
        expression (str): A string representing a matrix. It can be formed using [], {} or ().

    Returns:
        Matrix: The matrix the expression represents.

    Raises:
        ValueError if the format is invalid.
    """
    expr = re.sub(r"\ +", r"", expression)
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
