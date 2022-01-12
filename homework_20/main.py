from iter import HowIter


class Iter:

    def __init__(self, sequence):
        self.__sequence = sequence

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    one = Iter("One")
    five = Iter("Five")
    ten = Iter("Ten")
    seventh = Iter("Seventh")
    eight = Iter("Eight")

    list_iter = HowIter(start=0, stop=0, sequence=0)
    list_iter.add_to_list([one, five, ten, seventh, eight])

    for i in list_iter:
        print(i)
