import pytest

from calc import Calculator

def test_sum():
    assert Calculator(3, 2).sum() == 5

def test_subtract():
    assert Calculator(3, 2).subtract() == 1

def test_multiply():
    assert  Calculator(3, 2).multiply() == 6

def test_divide():
    assert Calculator(6, 2).divide() == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        Calculator(6, 0).divide()
    assert str(exc_info.value) == "Zero Division"

def test_missing_argument():
    with pytest.raises(ValueError) as exc_info:
        Calculator(None, 2)
    assert str(exc_info.value) == "No value provided"

def test_bool_argument():
    with pytest.raises(TypeError) as exc_info:
        Calculator(True, 2)
    assert str(exc_info.value) == "Bool value is not a number"

def test_string_argument():
    with pytest.raises(ValueError) as exc_info:
        Calculator("abc", 2)
    assert str(exc_info.value) == "String 'abc' is not a number"