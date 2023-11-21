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
    or import and use the alias R from rational_number.py in place of RatNum.

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
        if numerator.__class__ == RatNum:
            top *= numerator._numerator
            bot *= numerator._denominator
        else:
            top *= numerator
        if denominator.__class__ == RatNum:
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

        # negative / negative = positive
        if dd < 0 and ds < 0:
            dd, ds = abs(dd), abs(ds)
        # move negative from denominator to numerator
        if ds < 0 and dd > 0:
            dd, ds = -dd, -ds

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
        if ds < 0 and dd > 0:
            dd, ds = -dd, -ds

        reducer = gcd(dd, ds)
        return RatNum(dd // reducer,
                      ds // reducer)



    def __neg__(self) -> RatNum:
        return RatNum(-self._numerator, self._denominator)



    def __mul__(self, __mult: RatNum | int) -> RatNum | float:
        if __mult.__class__ is int :
            return RatNum(self._numerator * __mult,
                     self._denominator)
        elif __mult.__class__ is RatNum:
            return RatNum(self._numerator * __mult._numerator,
                          self._denominator * __mult._denominator)
        elif __mult.__class__ is float:
            return (self._numerator / self._denominator) * __mult
        else:
            TypeError(f"can't multiply RatNum by object of type {__mult.__class__}")

    def __rmul__(self, __mult: RatNum | int ) -> RatNum:
        return self.__mul__(__mult)



    def __truediv__(self, __div: RatNum | int) -> RatNum:
        if __div.__class__ == int:
            return RatNum(self._numerator, self._denominator * __div)

        elif __div.__class__ == RatNum:
            return RatNum(self._numerator * __div._denominator,
                          self._denominator * __div._numerator)

    def __rtruediv__(self, __div: RatNum | int) -> RatNum:
        return self.__truediv__(__div)



    def __add__(self, __num: RatNum | int) -> RatNum:
        if __num.__class__ == int:
            return RatNum(self._numerator + __num * self._denominator,
                          self._denominator)

        if __num.__class__ == RatNum:
            if __num._denominator == self._denominator:
                return RatNum(self._numerator + __num._numerator,
                              self._denominator)
            else:
                return RatNum((self._numerator * __num._denominator +
                              __num._numerator * self._denominator),
                              self._denominator * __num._denominator)

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
        if __num.__class__ == int and self._denominator == 1:
            return self._numerator == __num

        if __num.__class__ == RatNum:
            if self._numerator == __num._numerator and self._denominator == __num._denominator:
                return True

        return False

    def __req__(self, __num: RatNum | int) -> bool:
        return self.__eq__(__num)

    def __lt__(self, __num: RatNum | int) -> bool:
        if __num.__class__ == int:
            if __num * self._denominator > self._numerator:
                return True

        # TODO: may not work properly with rational numbers with small differences.
        if __num.__class__ == RatNum:
            if self._numerator / self._denominator > __num._numerator / __num._denominator:
                return True

        return False

    def __gt__(self, __num: RatNum | int) -> bool:
        if __num.__class__ == int:
            if __num * self._denominator < self._numerator:
                return True

        # TODO: may not work properly with rational numbers with small differences.
        if __num.__class__ == RatNum:
            if self._numerator / self._denominator < __num._numerator / __num._denominator:
                return True

        return False

    def __le__(self, __num: RatNum | int) -> bool:
        if self.__eq__(__num) or self.__lt__(__num):
            return True
        return False

    def __ge__(self, __num: RatNum | int) -> bool:
        if self.__eq__(__num) or self.__gt__(__num):
            return True
        return False



    def __str__(self) -> str:
        """Returns the rational number as a string, e.g. "22/7"."""
        r = self.reduced()

        if r._numerator == 0:
            return "0"
        elif r._denominator == 1:
            return str(r._numerator)

        return f"{r._numerator}/{r._denominator}"

    def __repr__(self) -> str:
        return self.__str__()

R: TypeAlias = RatNum
