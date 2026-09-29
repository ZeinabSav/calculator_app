from dataclasses import dataclass
from app.operation.operations import add, subtract, multiply, divide

@dataclass
class Calculation:
    a: float
    b: float
    operation_name: str
    result: float

class CalculationFactory:
    @staticmethod
    def create(a, b, operation_name):
        operations = {
            "add": add,
            "sub": subtract,
            "mul": multiply,
            "div": divide
        }

        if operation_name not in operations:
            raise ValueError("Unknown operation")

        func = operations[operation_name]
        result = func(a, b)
        return Calculation(a, b, operation_name, result)
