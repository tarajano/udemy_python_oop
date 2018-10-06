

"""
Python allows mutiple inheritance, therefore a 'diamond' situation can 
occur when one clas inherits from more than one parent.
Python uses Method Resolution Order  - see Class.mro() - to manage
possible congflicts.

Here I will create a multiple inheritance situation to test.
""" 

class GrandGrandParent(object):

    def __init__(self, value = None):
        self.specie = 'Human'
        if not value:
            self.origin = 'African'

    @classmethod # Class method Decorator
    def iam(cls):
        return cls.__name__

    def get_origin(self):
        return self.origin

    def get_specie(self):
        return self.specie


class ParentA(GrandGrandParent):
    def __init__(self, value = None):
        if not value:
            self.origin = 'Asian'

        super().__init__(self.origin)
        self.hair_color = 'Black'


class ParentB(GrandGrandParent):
    def __init__(self, value = None):
        if not value:
            self.origin = 'Nordic'
             
        super().__init__(self.origin)
        self.hair_color = 'Blond'


class Child(ParentA, ParentB):
    def __init__(self, value = None):
        self.origin = value
        super().__init__(self.origin)


c = Child('Latin')
print(c.iam())
print(c.get_origin())
print(c.get_specie())
print(Child.mro())


