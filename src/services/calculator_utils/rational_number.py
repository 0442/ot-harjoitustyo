from __future__ import annotations
from typing import TypeAlias

from math import gcd


class RatNum:
    """A rational number.

    Implements operations between rational numbers and ints,
    keeping track of the exact value of the rational number.
    Operations with floats will result in a float, meaning
    the exact value is lost.

    The rational number is also reduced after every operation.

    It is likely convenient to alias the class to a shorter name,
    e.g.
    ```
        from typing import TypeAlias
        from rational_number import RatNum

        SomeShortAliasName: TypeAlias = RatNum
    ```
    or import and use the alias Rn from rational_number.py in place of RatNum.

    Attributes:
    -----------
        numerator:
            The numerator of the rational number.
        denominator:
            A non-zero denominator of the rational number. If not given, defaults to 1.
    """

    def __init__(
        self,
        numerator: RatNum | int,
        denominator: RatNum | int = 1
    ) -> None:

        if denominator == 0:
            raise ZeroDivisionError("divison by zero")

        # If numerator or denominator is a rational number, reduce to a single rational number.
        top = 1
        bot = 1
        if numerator.__class__ is RatNum:
            top *= numerator._numerator
            bot *= numerator._denominator
        else:
            top *= numerator
        if denominator.__class__ is RatNum:
            top *= denominator._denominator
            bot *= denominator._numerator
        else:
            bot *= denominator

        self._numerator: RatNum | int = top
        self._denominator: RatNum | int = bot
        self.reduce()

    def reduce(self) -> None:
        """Bring this rational number into reduced form. Returns None."""

        # Cannot use self.reduced(), as this creates a new RatNum,
        # causing infinite recursion [this method is called in __init__()].

        dd = self._numerator
        ds = self._denominator

        # Negative / negative = positive.
        if dd < 0 and ds < 0:
            dd, ds = abs(dd), abs(ds)
        # Move negative from denominator to numerator.
        elif ds < 0 < dd:
            dd, ds = -dd, -ds
        # If nominator is 0, denominator's sign doesn't matter.
        elif dd == 0:
            ds = 1

        reducer = gcd(dd, ds)
        self._numerator = dd // reducer
        self._denominator = ds // reducer

    def reduced(self) -> RatNum:
        """Return a copy of this RatNum in the the reduced form."""
        dd = self._numerator
        ds = self._denominator

        # negative / negative = positive
        if dd < 0 and ds < 0:
            dd, ds = abs(dd), abs(ds)
        # move negative from denominator to numerator
        elif ds < 0 < dd:
            dd, ds = -dd, -ds
        # If nominator is 0, denominator's sign doesn't matter.
        elif dd == 0:
            ds = 1

        reducer = gcd(dd, ds)
        return RatNum(dd // reducer,
                      ds // reducer)

    def __neg__(self) -> RatNum:
        return RatNum(-self._numerator, self._denominator)

    def __mul__(self, __num: RatNum | int) -> RatNum | float:
        if __num.__class__ is int:
            return RatNum(self._numerator * __num,
                          self._denominator)
        if __num.__class__ is RatNum:
            return RatNum(self._numerator * __num._numerator,
                          self._denominator * __num._denominator)
        if __num.__class__ is float:
            return (self._numerator / self._denominator) * __num

        raise TypeError((f"unsupported operand type(s) for *: "
                         f"'{self.__class__}' and '{__num.__class__}'"))

    def __rmul__(self, __num: RatNum | int) -> RatNum:
        return self.__mul__(__num)

    def __truediv__(self, __num: RatNum | int) -> RatNum:
        if __num.__class__ is int:
            return RatNum(self._numerator, self._denominator * __num)

        if __num.__class__ is RatNum:
            return RatNum(self._numerator * __num._denominator,
                          self._denominator * __num._numerator)

        raise TypeError((f"unsupported operand type(s) for /: "
                         f"'{self.__class__}' and '{__num.__class__}'"))

    def __rtruediv__(self, __div: RatNum | int) -> RatNum:
        return self.__truediv__(__div)

    def __add__(self, __num: RatNum | int) -> RatNum:
        if __num.__class__ is int:
            return RatNum(self._numerator + __num * self._denominator,
                          self._denominator)

        if __num.__class__ is RatNum:
            if __num._denominator == self._denominator:
                return RatNum(self._numerator + __num._numerator,
                              self._denominator)

            return RatNum((self._numerator * __num._denominator +
                           __num._numerator * self._denominator),
                          self._denominator * __num._denominator)

        raise TypeError((f"unsupported operand type(s) for +: "
                         f"'{self.__class__}' and '{__num.__class__}'"))

    def __radd__(self, __num: RatNum | int) -> RatNum:
        return self.__add__(__num)

    def __sub__(self, __num: RatNum | int) -> RatNum:
        return self.__add__(-__num)

    def __rsub__(self, __num: RatNum | int) -> RatNum:
        return self.__sub__(__num)

    def __pow__(self, __power: int) -> RatNum:
        return RatNum(self._numerator**__power,
                      self._denominator**__power)

    def __eq__(self, __num: RatNum | int) -> bool:

        # Rational number can equal an integer only when the denominator is 1.
        # self._denominator is always 1 when this RatNum can be considered an
        # int as RatNums are reduced after every calculation.
        if __num.__class__ is int and self._denominator == 1:
            return self._numerator == __num

        if __num.__class__ is RatNum:
            return self._numerator == __num._numerator and self._denominator == __num._denominator

        return False

    def __req__(self, __num: RatNum | int) -> bool:
        return self.__eq__(__num)

    def __lt__(self, __num: RatNum | int) -> bool:
        if __num.__class__ is int:
            return __num * self._denominator > self._numerator

        if __num.__class__ is RatNum:
            # Scale to same denominator and then compare numerators
            return self._numerator * __num._denominator < __num._numerator * self._denominator

        return False

    def __gt__(self, __num: RatNum | int) -> bool:
        if __num.__class__ in (RatNum, int):
            return not self.__lt__(__num) and __num != 0

        return False

    def __le__(self, __num: RatNum | int) -> bool:
        return self.__eq__(__num) or self.__lt__(__num)

    def __ge__(self, __num: RatNum | int) -> bool:
        return self.__eq__(__num) or self.__gt__(__num)

    def __str__(self) -> str:
        """Returns the rational number as a string, e.g. "22/7"."""
        r = self.reduced()

        if r._numerator == 0:
            return "0"

        if r._denominator == 1:
            return str(r._numerator)

        return f"{r._numerator}/{r._denominator}"

    def __repr__(self) -> str:
        return self.__str__()


Rn: TypeAlias = RatNum
