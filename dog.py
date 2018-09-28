
from animal import Animal

class Dog(Animal):

    def fetch(self, thing):
        print("{} fetches a {}".format(self.get_name(), thing))
