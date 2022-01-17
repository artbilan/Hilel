from apple import Apple
from banan import Banan
from strawbarry import Strawbarry
from celery import Celery


class GetProduct:
    @staticmethod
    def get_product(type: str):
        if type == "apple":
            return Apple()
        elif type == "banan":
            return Banan()
        elif type == "strawbarry":
            return Strawbarry
        elif type == "celery":
            return Celery
        else:
            raise Exception("wrong item")

