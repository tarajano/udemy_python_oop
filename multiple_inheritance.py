

"""
Python allows mutiple inheritance, therefore a 'diamond' situation can 
occur when one clas inherits from more than one parent.
Python uses Method Resolution Order  - see Class.mro() - to manage
possible congflicts.

Here I will create a multiple inheritance situation to test.
""" 

class GrandGrandParent(object):
    @classmethod # Class method Decorator
    def iam(cls):
        return cls.__name__
    
    def get_origin(cls):
        return 'African'

    @staticmethod # Static is used for 'utility'  methods
    def get_specie(cls):
        return 'Human'


class ParentA(GrandGrandParent):
    
    def get_origin(self):
        return 'European' 
        

class ParentB(GrandGrandParent):

    def get_origin(self):
        return 'Arabic' 


class Child(ParentA, ParentB):
    pass


c = Child()
print(c.iam())
print(c.get_origin())
print(c.get_specie())
print(Child.mro())


# TODO .. INVESTIGATE DIFFERENCE BETWEEN @CLASSMETHOD AND @STATICMETHOD decorators
