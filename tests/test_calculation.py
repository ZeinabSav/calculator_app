import pytest
from app.calculation.calculation import CalculationFactory, Calculation

def test_create_add():
    calc = CalculationFactory.create(2, 3, "add")
    assert isinstance(calc, Calculation)
    assert calc.result == 5

def test_create_sub():
    calc = CalculationFactory.create(5, 2, "sub")
    assert calc.result == 3

def test_create_mul():
    calc = CalculationFactory.create(4, 3, "mul")
    assert calc.result == 12

def test_create_div():
    calc = CalculationFactory.create(10, 2, "div")
    assert calc.result == 5

def test_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create(1, 1, "unknown")

def test_square_calc():
    calc = CalculationFactory.create(4, None, "square")
    assert calc.result == 16

from app.operation.operations import (
    add, subtract, multiply, divide,
    square, power, modulo, sqrt, absolute
)

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = self.operation(a) if b is None else self.operation(a, b)

class CalculationFactory:
    @staticmethod
    def create(a, b, operation_name):
        operations = {
            "add": add,
            "sub": subtract,
            "mul": multiply,
            "div": divide,
            "square": square,
            "pow": power,
            "mod": modulo,
            "sqrt": sqrt,
            "abs": absolute
        }

        if operation_name not in operations:
            raise ValueError("Unknown operation")

        operation = operations[operation_name]
        return Calculation(a, b, operation)



    