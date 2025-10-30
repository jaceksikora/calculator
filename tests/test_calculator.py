import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

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
    calc = Calculator(6, 0)
    assert calc.divide() == "Dzielenie przez zero"

def test_invalid_arguments():
    with pytest.raises(TypeError):
        Calculator("abc", 2)
