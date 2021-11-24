from typing import Callable


def smart_divide(func: Callable) -> Callable:
    print(f'start function is {smart_divide.__name__}')

    def inner(a: int, b: int) -> Callable:
        print(f'start function is {inner.__name__}')
        return func(a, b)
    return inner


@smart_divide
def divide(a: int, b: int) -> str:
    print(f'result decoration func is {a/b}')


divide(9, 5)
