
def calculate(a: float, b: float, operation: str) -> float:
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
    else:
        raise ValueError("Unsupported operation")

    if not __import__("math").isfinite(result):
        raise ValueError("Result is outside the supported range")

    return result
