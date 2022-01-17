

class Human:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @staticmethod
    def __validate_gender(gender):
        if gender not in ["male", "female"]:
            raise Exception("Not supported gender")
        else:
            return gender

    def grow(self):
        self.__age += 1

    def change_name(self, name):
        if name != self.__name:
            self.__name = name
        else:
            raise Exception("Provided name is same as current")

    def change_gender(self, gender):
        self.__gender = self.__validate_gender(gender)

    def return_age(self):
        return self.__age
