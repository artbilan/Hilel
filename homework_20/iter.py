class HowIter:

    def __init__(self, start=0, stop=0, sequence=0):
        self.__new_list = []
        self.__current = start
        self.__start = start
        self.__stop = stop
        self.__sequence = sequence

    def to_add(self, item):
        self.__new_list.append(item)

    def add_to_list(self, new_lists: list):
        self.__new_list.extend(new_lists)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__sequence > 0:

            if self.__current - 1 == self.__stop and self.__stop > 0 and self.__sequence > 0:
                raise StopIteration
            if len(self.__new_list) > self.__current:
                item = self.__new_list[self.__current]
                self.__current += self.__sequence
                return item
            else:
                raise StopIteration
        else:
            if self.__current - 1 == self.__stop and self.__stop > 0:
                raise StopIteration
            if len(self.__new_list) > self.__current:
                item = self.__new_list[self.__current]
                self.__current += 1
                return item
            else:
                raise StopIteration
