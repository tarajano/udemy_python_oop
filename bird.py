
from animal import Animal

class Bird(Animal):

    def __init__(self, name):
        super(Bird, self).__init__(name)
        self.name = name

    def chants(self, chant):
        return "{} chants {}".format(self.get_name(), chant)
