import calculator
import pytest


def test_addition():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(6, 3) == 3
    assert calculator.subtract(6, 10) == -4

def test_multiply():
    assert calculator.multiply(6, 3) == 18
    assert calculator.multiply(6, 0) == 0

def test_divide():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
    assert calculator.divide(6, 3) == 2
