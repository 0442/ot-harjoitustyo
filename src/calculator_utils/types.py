from typing import TypeAlias

from calculator_utils.rational_number import Rn

Num: TypeAlias = Rn | int
Matrix: TypeAlias = list[list[Rn | int]]
RowVector: TypeAlias = list[Rn | int]
