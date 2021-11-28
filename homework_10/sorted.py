from functools import reduce
from typing import Callable

number = [-5, 1, 2, 3, 0]

print(reduce(lambda arg1, arg2: arg1 if arg1 > arg2 else arg2, number))
