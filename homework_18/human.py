from abc import ABC, abstractmethod


class Human(ABC):

    def __init__(self, sex: str, color: str):
        self.__type = sex
        self.__color = color

    def do_walk(self):
        raise Exception(f'Method {self.do_walk} missing in {self.__class__.__name__}')

    def do_eat(self):
        raise Exception(f'Method {self.do_eat} missing in {self.__class__.__name__}')

    @abstractmethod
    def do_work(self):
        pass
