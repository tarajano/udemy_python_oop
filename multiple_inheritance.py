

"""
Python allows mutiple inheritance, therefore a 'diamond' situation can 
occur when one clas inherits from more than one parent.
Python uses Method Resolution Order  - see Class.mro() - to manage
possible congflicts.

Here I will create a multiple inheritance situation to test.
""" 

class Specie(object):
    def iam(self):
        return Specie.__name__
    
    def get_origin(self):
        return 'African'

    def get_specie(self):
        return 'Human'


class ParentA(Specie):
    def iam(self):
        return ParentA.__name__
    
    def get_origin(self):
        return 'European' 
        

class ParentB(Specie):
    def iam(self):
        return ParentB.__name__

    def get_origin(self):
        return 'Arabic' 



class Child(ParentA, ParentB):
    def iam(self):
        return Child.__name__


c = Child()
print(c.iam())
print(c.get_origin())
print(c.get_specie())
print(Child.mro())

