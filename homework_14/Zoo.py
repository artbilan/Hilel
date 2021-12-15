class Zoo:
    def __init__(self, name: str, type: str, country: str, avairy: int)-> None:
        self.name = name
        self.type = type
        self.country = country
        self._avairy = avairy
        return print(f'{self.name} is created')


    @classmethod
    def update_avairy(cls, number):
        cls.avairy = number
        return print(f'new avairy is {cls.avairy}')


tiger = Zoo("tiger", "mammals", "Mozambique", 177)

tiger.update_avairy(257)

c = tiger.avairy
print(c)