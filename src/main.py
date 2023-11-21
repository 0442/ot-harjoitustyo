from typing import TypeAlias
from random import randint

from matrix.rational_number import RatNum

R: TypeAlias = RatNum

def random_ratnum_sum():
    nums = [R(randint(-99, 99), randint(1,99)) for _ in range(3)]

    string = []
    for i,n in enumerate(nums):
        if i != 0:
            if n >= 0:
                string.append(" + " + str(n))
            else:
                string.append(" - " + str(n).removeprefix("-"))
        else:
            string.append(str(n))

    return f"{''.join(string)} = {sum(nums)}"

if __name__ == "__main__":
    print(random_ratnum_sum())
