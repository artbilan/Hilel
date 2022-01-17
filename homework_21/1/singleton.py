from typing import Type


def singleton(_type: Type):
    def decoratee(number):
        if hasattr(_type, "_instance"):
            return getattr(_type, "_instance")
        else:
            instance = _type(number)
            setattr(_type, "_instance", instance)
            return getattr(_type, "_instance")
    return decoratee
