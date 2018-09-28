
from animal import Animal

class Cat(Animal):

    def chase(self, thing):
        print("{} chases a {}".format(self.get_name(), thing))

