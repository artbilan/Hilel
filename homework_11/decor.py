from typing import Callable


def smart_divide(func: Callable) -> Callable:
    print(f'start from function {smart_divide.__name__}')

    def inner(a: int, b: int) -> Callable:
        return func(a, b)
    return inner


@smart_divide
def div(a: int, b: int) -> str:
    print(f'result is {a/b}')

div(9, 13)

