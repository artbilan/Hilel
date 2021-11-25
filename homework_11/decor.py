from typing import Callable


def smart_divide(func: Callable) -> Callable:
    def inner(a: int, b: int) -> Callable:
        print(f'start from function "{inner.__name__}"')
        return func(a, b)
    return inner


@smart_divide
def divide(a: int, b: int) -> str:
    print(f'result decoration func is {a/b}')


divide(9, 5)
