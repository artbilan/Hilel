number = [1, 2, 3, 4, 5, 6, 7, 8]

def new_reduce(x, operand):

a = 0

for i in number:
    if a == 0:
        a = number[0]
    a = a - i
print(a)
