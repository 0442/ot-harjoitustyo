from random import randint
import ui.ui

from matrix.rational_number import Rn


def ratnum_demo():
    nums = [Rn(randint(-99, 99), randint(1, 99)) for _ in range(3)]

    string = []
    for i, n in enumerate(nums):
        if i != 0:
            if n >= 0:
                string.append(" + " + str(n))
            else:
                string.append(" - " + str(n).removeprefix("-"))
        else:
            string.append(str(n))

    print(f"{''.join(string)} = {sum(nums)}")


if __name__ == "__main__":
    ratnum_demo()
