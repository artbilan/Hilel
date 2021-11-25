number = [5, 10, 20]

def new_reduce(some_list: list, operand: str)-> str:
    a = 0
    if operand == "-":
        for i in some_list:
            if a == 0:
                a = some_list[0]
            a = a - i
    elif operand == "+":
        for i in some_list:
            a = a + i
    elif operand == "*":
        if a == 0:
            a = 1
            for i in some_list:
                a = a * i
    return a



cc = new_reduce(number, "-")
print(cc)
