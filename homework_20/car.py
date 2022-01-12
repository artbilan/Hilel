from modification import ChipTuning
from abc import abstractmethod


class Car:

    def __init__(self, brand: str, type: str) -> None:
        self.__brand = brand
        self.__type = type

    def __str__(self):
        return f'car brand is: {self.__brand}\ncar type is: {self.__type}'

    @abstractmethod
    def power_on(self):
        power = True
        return power

    @abstractmethod
    def power_off(self):
        power = False
        return power

    @ChipTuning
    def modification(hp: int):
        return hp


if __name__ == "__main__":
    a = Car
    print(a.modification(500))
