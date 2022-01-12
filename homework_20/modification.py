
class ChipTuning:

    def __init__(self, function):
        self.__function = function

    def __call__(self, hp: int):
        return f'new car horse power is: {self.__function(hp * 1.25)}'
