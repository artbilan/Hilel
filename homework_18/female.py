from human import Human

class Female(Human):


    def do_talk(self):
        return f'{self.__class__.__name__} is talk'

    def do_breath(self):
        return f'{self.do_breath} is breath'


    def do_work(self):
        return f'{__class__.__name__} work in factory'
