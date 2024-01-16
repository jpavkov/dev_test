# a good example of multiple inheritance bc Flyer and Swimmer are abstract and simple

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
