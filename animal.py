

class Animal(object):

    def __init__(self, arg):
        # super(Animal, self).__init__, name()
        self.name = arg

    def get_name(self):
        return self.name

    def eats(self, food):
        return "{} eats lots of {}".format(self.name, food)

    

        