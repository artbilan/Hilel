class Carbone:

    def __init__(self):
        self.name = 'Carbone'
        self.formula = "C"

    def __str__(self):
        return f'formula for {self.name}: {self.formula}'

    def do_print(self):
        return (self.formula)

    def __add__(self, other):
        return f'formula for {self.name} + {other.name}: {self.formula + other.formula}'

    def __radd__(self, other):
        return f'formula for {other.name} + {self.name}: {self.formula + other.formula}'


