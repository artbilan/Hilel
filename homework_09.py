def arithmetic(a:float, b:float, operation:str)-> float or str:
    if operation == "+":
        x = a + b
        return x
    elif operation == "-":
        x = a - b
        return x
    elif operation == "*":
        x = a * b
        return x
    elif operation == "/":
        x = a / b
        return x
    else:
        return f'Not known operation: {operation}'

calc = arithmetic(7, 10, "*")
print(calc)