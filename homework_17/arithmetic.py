def arithmetic(a: float, b: float, operation:str):

    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return f'Not known operation: {operation}'
