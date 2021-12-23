from Dog import Dog


class Mastif(Dog):
    def __init__(self, name: str, color: str, owner: str) -> None:
        super().__init__(self, color)
        self.__name = name
        self.__owner = owner

    def new_owner(self, new_owner: str):
        self.owner = new_owner
        return f"new owner is {new_owner}"


Albert = Mastif("Bars", "Dark", "Alberto")

owner_alberto = Mastif.new_owner(Mastif, "Alberto")
print(owner_alberto)

Al = Mastif.bark("Al")
