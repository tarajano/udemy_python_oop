
import pickle
from animal import Animal

name = 'Manuel'
me = Animal(name)


with open('pickle_file.pkl', 'wb') as pf:
    pickle.dump(me, pf)

with open('pickle_file.pkl', 'rb') as pf:
    me2 = pickle.load(pf)

print('Animal: {}'.format(me2.get_name()))

