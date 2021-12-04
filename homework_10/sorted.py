def new_sorted(x: list, reverse=False) -> list:
    if reverse is False:
        for i in range(len(x)-1):
            for i2 in range(len(x)-1-i):
                if x[i2] > x[i2+1]:
                    x[i2], x[i2+1] = x[i2+1], x[i2]
    elif reverse is True:
        for i in range(len(x)-1):
            for i2 in range(len(x)-1-i):
                if x[i2] > x[i2+1]:
                    x[i2], x[i2+1] = x[i2+1], x[i2]
                    x.reverse()
    return x


numbers = [1, 0, 5, -10, 50, -100]
new_numbers = new_sorted(numbers, reverse=False)
print(new_numbers)
