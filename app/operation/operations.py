

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_square_calc():
    calc = CalculationFactory.create(4, None, "square")
    assert calc.result == 16
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

def test_square():
    assert square(4) == 16

def test_power():
    assert power(2, 3) == 8

def test_modulo():
    assert modulo(10, 3) == 1

def test_sqrt():
    assert sqrt(9) == 3

def test_absolute():
    assert absolute(-5) == 5
