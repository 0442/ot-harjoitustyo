from re import sub

from calculator.utils.row_echelon import reduced_row_echelon
from calculator.utils.rational_number import Rn


def str_to_num(num_str: str):
    if num_str.count("/") == 1:
        rn = num_str.split("/")
        return Rn(int(rn[0]), int(rn[1]))

    return int(num_str)


def str_to_matrix(expression: str):
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
    """High-level class which UI utilizes to perform tasks."""

    def __init__(self) -> None:
        self._user = None

    def find_row_reduce(self, expression: str) -> str:
        expression = str_to_matrix(expression)
        result = reduced_row_echelon(expression, [])
        return str(result)

    def get_history(self) -> list[str] | None:
        if self._user is None:
            return None
        return []
