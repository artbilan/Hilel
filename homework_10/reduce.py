from typing import Callable
from functools import reduce

number = [1, 2, 3, 4, 5]

print(reduce(lambda arg1, arg2: arg1 - arg2, number))


