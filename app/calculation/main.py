from app.calculation.calculation import CalculationFactory

def print_help():
    print("Commands:")
    print("  add/sub/mul/div a b")
    print("  history")
    print("  help")
    print("  exit")

def repl():
    history = []
    print("Welcome to the calculator! Type 'help' for commands.")

    while True:
        user_input = input("> ").strip()

        if user_input == "exit":
            print("Goodbye!")
            break

        if user_input == "help":
            print_help()
            continue

        if user_input == "history":
            for calc in history:
                print(f"{calc.operation_name}({calc.a}, {calc.b}) = {calc.result}")
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format. Use: operation a b")
            continue

        op, a_str, b_str = parts

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid numbers.")
            continue

        try:
            calc = CalculationFactory.create(a, b, op)
        except Exception as e:
            print(f"Error: {e}")
            continue

        history.append(calc)
        print(f"Result: {calc.result}")

if __name__ == "__main__":
    repl()
def print_help():
    print("Commands:")
    print("  add/sub/mul/div a b")
    print("  square a")
    print("  pow a b")
    print("  mod a b")
    print("  sqrt a")
    print("  abs a")
    print("  history")
    print("  help")
    print("  exit")
