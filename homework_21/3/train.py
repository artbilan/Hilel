
class Train:

    def __init__(self, car_train_amount: int):
        self.__car_train_amount = car_train_amount
        self.__base_amount = 0

    def add_car_train(self, new_number):
        return self.__base_amount + new_number

    def __str__(self):
        return f'car train in train is {self.__car_train_amount}'

    def __len__(self):
        return self.__car_train_amount - 1






