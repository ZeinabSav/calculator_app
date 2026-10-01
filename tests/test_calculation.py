from app.calculation.calculation import CalculationFactory, Calculation
import pytest

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
