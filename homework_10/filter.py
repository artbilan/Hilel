from typing import Callable


def new_filter(func: Callable, li: list) -> list:
    new_list = []
    for i in li:
        if func(i):
            new_list.append(i)
    return new_list


number = [-7, 6, 0, 2, 100, 47]

cc = new_filter(lambda x: x > 5, number)
print(cc)
