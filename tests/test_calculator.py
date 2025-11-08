import pytest

from calc import Calculator

def test_sum():
    calc = Calculator(3, 2)
    assert calc.sum() == 5

def test_subtract():
    calc = Calculator(3, 2)
    assert calc.subtract() == 1

def test_multiply():
    calc = Calculator(3, 2)
    assert calc.multiply() == 6

def test_divide():
    calc = Calculator(6, 2)
    assert calc.divide() == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        Calculator(6, 0).divide()
    assert str(exc_info.value) == "Zero Division"

def test_invalid_arguments():
    with pytest.raises(ValueError) as exc_info:
        Calculator("abc", 2)
    assert str(exc_info.value) == "String 'abc' is not a number"