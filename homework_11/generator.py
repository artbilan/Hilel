def func_sq(x: int) -> int:
    counter = 0
    while counter < x:
        if counter % 2 == 0:
            yield counter ** 2
        counter += 1


generator = func_sq(1000000000)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
