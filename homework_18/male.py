from human import Human


class Male(Human):

    def do_work(self):
        return f'{__class__.__name__} work in factory'
