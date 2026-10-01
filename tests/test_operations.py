from app.operation.operations import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

import math

def square(a):
    return a * a

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero")
    return a % b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def absolute(a):
    return abs(a)
