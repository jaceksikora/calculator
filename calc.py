from __future__ import annotations
from decimal import Decimal
from fractions import Fraction
from typing import Union

NumberLike = Union[int, float, Decimal, Fraction, bool, str]

class Calculator:
    def __init__(self, op1: NumberLike, op2: NumberLike):
        self.op1 = self._validate_number_input_(op1)
        self.op2 = self._validate_number_input_(op2)

    @staticmethod
    def _validate_number_input_(value: NumberLike) -> float:
        if value is None:
            raise ValueError("No value provided")

        if isinstance(value, bool):
            raise TypeError("Bool value is not a number")

        if isinstance(value, (int, float, Decimal, Fraction)):
            return float(value)

        if isinstance(value, str):
            s = value.strip()
            try:
                return float(s)
            except (ValueError, TypeError):
                raise ValueError(f"String '{value}' is not a number")

        raise TypeError(f"Unsupported type: {type(value).__name__}. Please provide numeric value")

    def sum(self) -> float:
        return self.op1 + self.op2

    def subtract(self) -> float:
        return self.op1 - self.op2

    def multiply(self) -> float:
        return self.op1 * self.op2

    def divide(self) -> float | str:
        if self.op2 == 0:
            raise ZeroDivisionError("Zero Division")
        return self.op1 / self.op2


if __name__ == '__main__':
    print(Calculator(0, 2.3).sum())
    print(Calculator(0, "2.3").sum())
    print(Calculator(0, 2.4).subtract())
    print(Calculator(0, 2.5).multiply())

    print(Calculator(0, 0).divide())
    print(Calculator(0, 2).divide())
    print(Calculator(2, 0).divide())
