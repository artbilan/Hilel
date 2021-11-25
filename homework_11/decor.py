from typing import Callable


def smart_divide(func: Callable) -> Callable:
    def inner(a: int, b: int) -> Callable:
        return func(a, b)
    return inner


@smart_divide
def divide(a: int, b: int) -> str:
    print(f'function start from function "{divide.__name__}"')
    print(f'result decoration func is {a/b}')


divide(9, 5)
