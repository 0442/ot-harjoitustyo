from __future__ import annotations
from typing import TypeAlias

from math import gcd


class RatNum:
    """A rational number.

    Implements operations between rational numbers and ints,
    keeping track of the exact value of the rational number.

    The rational number is reduced after every operation.

    It is likely convenient to alias the class to a shorter name,
    e.g.
    ```
        from typing import TypeAlias
        from rational_number import RatNum

        SomeShortAliasName: TypeAlias = RatNum
    ```
    or import the alias `Rn` from rational_number.py in place of `RatNum`.

    """

    def __init__(
        self,
        numerator: RatNum | int,
        denominator: RatNum | int = 1
    ) -> None:
        """
        Args:
            numerator (RatNum | int): The numerator of the rational number.
            denominator (RatNum | int, optional): A non-zero denominator of
            the rational number. Defaults to 1.

        Raises:
            ZeroDivisionError: If denominator is 0.
        """

        if denominator == 0:
            raise ZeroDivisionError("divison by zero")

        # If numerator or denominator is a rational number, reduce to a single rational number.
        top = 1
        bot = 1
        if isinstance(numerator, RatNum):
            top *= numerator._numerator
            bot *= numerator._denominator
        else:
            top *= numerator
        if isinstance(denominator, RatNum):
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

    def __mul__(self, _num: RatNum | int) -> RatNum:
        if isinstance(_num, int):
            return RatNum(self._numerator * _num,
                          self._denominator)
        if isinstance(_num, RatNum):
            return RatNum(self._numerator * _num._numerator,
                          self._denominator * _num._denominator)

        raise TypeError((f"unsupported operand type(s) for *: "
                         f"'{self.__class__}' and '{_num.__class__}'"))

    def __rmul__(self, _num: RatNum | int) -> RatNum:
        return self.__mul__(_num)

    def __truediv__(self, _num: RatNum | int) -> RatNum:
        if isinstance(_num, int):
            return RatNum(self._numerator, self._denominator * _num)

        if isinstance(_num, RatNum):
            return RatNum(self._numerator * _num._denominator,
                          self._denominator * _num._numerator)

        raise TypeError((f"unsupported operand type(s) for /: "
                         f"'{self.__class__}' and '{_num.__class__}'"))

    def __rtruediv__(self, _num: RatNum | int) -> RatNum:
        return self.__truediv__(_num)

    def __add__(self, _num: RatNum | int) -> RatNum:
        if isinstance(_num, int):
            return RatNum(self._numerator + _num * self._denominator,
                          self._denominator)

        if isinstance(_num, RatNum):
            if _num._denominator == self._denominator:
                return RatNum(self._numerator + _num._numerator,
                              self._denominator)

            return RatNum((self._numerator * _num._denominator +
                           _num._numerator * self._denominator),
                          self._denominator * _num._denominator)

        raise TypeError((f"unsupported operand type(s) for +: "
                         f"'{self.__class__}' and '{_num.__class__}'"))

    def __radd__(self, _num: RatNum | int) -> RatNum:
        return self.__add__(_num)

    def __sub__(self, _num: RatNum | int) -> RatNum:
        return self.__add__(-_num)

    def __rsub__(self, _num: RatNum | int) -> RatNum:
        return self.__sub__(_num)

    def __pow__(self, __power: int) -> RatNum:
        return RatNum(self._numerator**__power,
                      self._denominator**__power)

    def __eq__(self, _num: RatNum | int) -> bool:

        # Rational number can equal an integer only when the denominator is 1.
        # self._denominator is always 1 when this RatNum can be considered an
        # int as RatNums are reduced after every calculation.
        if isinstance(_num, int) and self._denominator == 1:
            return self._numerator == _num

        if isinstance(_num, RatNum):
            return self._numerator == _num.numerator and self._denominator == _num.denominator

        return False

    def __req__(self, _num: RatNum | int) -> bool:
        return self.__eq__(_num)

    def __lt__(self, _num: RatNum | int) -> bool:
        if isinstance(_num, int):
            return _num * self._denominator > self._numerator

        if isinstance(_num, RatNum):
            # Scale to same denominator and then compare numerators
            return self._numerator * _num.denominator < _num._numerator * self.denominator

        return False

    def __gt__(self, _num: RatNum | int) -> bool:
        if isinstance(_num, (RatNum, int)):
            return not self.__lt__(_num) and _num != 0

        return False

    def __le__(self, _num: RatNum | int) -> bool:
        return self.__eq__(_num) or self.__lt__(_num)

    def __ge__(self, _num: RatNum | int) -> bool:
        return self.__eq__(_num) or self.__gt__(_num)

    def __str__(self) -> str:
        """Returns the rational number as a string, e.g. "22/7"."""
        r = self.reduced()

        if r.numerator == 0:
            return "0"

        if r.denominator == 1:
            return str(r.numerator)

        return f"{r.numerator}/{r.denominator}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator


Rn: TypeAlias = RatNum
