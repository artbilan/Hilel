
class CarTrain:

    def __init__(self, name, destination, place):
        self.name = name
        self.destination = destination
        self.place = place
        self.total_passengers = self.add_passanger()

    @staticmethod
    def add_passanger():
        total = 0
        new_total = total + 1
        return new_total

    def __modify_private_key(self, key):
        return key.replace(f'_{self.__class__.__name__}__', "")

    def __str__(self):
        start = "{\n"
        content = ''
        end = '}'

        for key, value in self.__dict__.items():
            content += f'\t{self.__modify_private_key(key)}:{value}\n'

        return f'{start}{content[:len(content) - 1]}\n{end}'

    def __len__(self):
        return self.total_passengers


a = CarTrain("John", "New-York", "9f")
b = CarTrain("Marta", "Dallas", "10f")

print(b)

car_train = CarTrain("John", "New-York", "9f")
car_train.add_passanger()


print(len(a))
