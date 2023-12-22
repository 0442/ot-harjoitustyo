from calculator_utils.types import Num, Matrix
from config import LATEX_INDENT, LATEX_MAT_BEGIN, LATEX_MAT_END


def matrix_to_latex(matrix: Matrix) -> str:
    col_widths = _column_latex_widths(matrix)

    latex_lines = [LATEX_MAT_BEGIN]

    for row in matrix:
        new_line = LATEX_INDENT

        for col_i, elem in enumerate(row):
            elem_latex = _num_to_latex(elem)
            new_line += elem_latex.rjust(col_widths[col_i]) + r" & "

        new_line += r"\\"

        latex_lines.append(new_line)

    latex_lines += [LATEX_MAT_END]

    return '\n'.join(latex_lines)


def _num_to_latex(num: Num):
    """Returns a numbers latex representation.

    Useful for formatting rational numbers from "a/b" to "\\frac{a}/{b}" """
    num_str = str(num)
    if num_str.count("/") > 0:
        a = num_str.split("/")
        dividend, divisor = a[0], a[1]
        num_str = r"\frac{" + f"{dividend}" + r"}{" + f"{divisor}" + r"}"
    return num_str


def _column_latex_widths(matrix: Matrix):
    """
    Gets the width of the widest element (widest in LaTeX code), for each column in given matrix.

    Useful for aligning in LaTeX code.
    """
    width = len(matrix[0])
    height = len(matrix)

    col_widths = []

    for col_i in range(width):
        widest_elem = 0
        for row_i in range(height):
            e = matrix[row_i][col_i]
            widest_elem = max(len(str(e)), widest_elem)

        col_widths.append(widest_elem)

    return col_widths
