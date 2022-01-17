from singleton import singleton


@singleton
class GSMConnection:

    def __init__(self, number: int):
        self.__host = number

    @property
    def gsm_connection(self):
        return self._number


