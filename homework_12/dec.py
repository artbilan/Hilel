from typing import Callable
import time


def finish_time(function: Callable):

    def wrapper(factor: int, max_number: int):

        new_list = []
        start_time = time.time()
        for i in range(max_number):
            new_list.append(i**factor)
        finish_time = time.time() - start_time
        return f'finish time for factor {factor} and range {max_number} is - {finish_time} seconds'
    return wrapper


@finish_time
def func(a, b):
    pass


print(func(2, 10000))
