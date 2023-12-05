from calculator.utils.rational_number import Rn
from calculator.utils.matrix_utils import (
    validate_matrix,
    add_row,
    all_leading_nums_to_one,
    arrange_matrix,
    first_non_zero,
    Step
)


def row_echelon(matrix: list[list[Rn]], steps: list = None) -> list[list[Rn]]:
    """
    ValueError is raised if rows are of differing width.
    """
    if steps is None:
        steps = []

    height = len(matrix)
    validate_matrix(matrix)

    result_matrix = arrange_matrix(matrix)
    steps.append(Step("Arrange matrix", result_matrix[:]))

    # Make all nums below pivots zero.
    # Result is matrix in row echelon form.
    for pivot in range(height):
        pivot_row = result_matrix[pivot]

        pivot_col_i = first_non_zero(pivot_row)
        if pivot_col_i is None:
            # Row is a 0 row and
            # there must only be other 0 rows below,
            break

        for row_below_i in range(pivot+1, height):
            row_below = result_matrix[row_below_i]

            if row_below[pivot_col_i] != 0:
                scalar = -Rn(row_below[pivot_col_i], pivot_row[pivot_col_i])
                n_row = add_row(row_below,
                                pivot_row,
                                scalar)

                result_matrix[row_below_i] = n_row

                desc = (f"Add ${scalar}R_{(pivot+1)}$"
                        f" to $R_{(row_below_i+1)}$")
                steps.append(Step(desc, result_matrix[:]))
            else:
                # If there is a zero here on this row,
                # there must also be on the rows below.
                break

    return result_matrix


def reduced_row_echelon(matrix: list[list[Rn]], steps: list = None):
    if steps is None:
        steps = []

    rev_matrix = row_echelon(matrix, steps)
    rev_matrix.reverse()

    height = len(rev_matrix)

    for pivot in range(height):
        pivot_row = rev_matrix[pivot]

        pivot_col_i = first_non_zero(pivot_row)
        if pivot_col_i is None:
            # if pivot is not found, the row is a 0 row.
            # Continue because matrix is reversed here.
            continue

        for row_below_i in range(pivot+1, height):
            row_below = rev_matrix[row_below_i]

            if row_below[pivot_col_i] != 0:
                scalar = -Rn(row_below[pivot_col_i], pivot_row[pivot_col_i])
                new_row_below = add_row(row_below,
                                        pivot_row,
                                        scalar)
                rev_matrix[row_below_i] = new_row_below

                desc = (f"Subtract ${scalar}R_{height-(pivot+1)}$ "
                        f"from $R_{height-(row_below_i+1)}$")
                steps.append(Step(desc, list(reversed(rev_matrix[:]))))

    # Leading nums to one
    rev_matrix = all_leading_nums_to_one(rev_matrix, steps)

    # Reverse back to original matrix
    return list(reversed(rev_matrix))
