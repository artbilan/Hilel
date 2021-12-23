class Methane:

    def __init__(self):
        self.name = 'Methane'
        self.formula = "CH4"

    def __str__(self):
        return f'formula for {self.name}: {self.formula}'

    def do_print(self):
        return self.formula
