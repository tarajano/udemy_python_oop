
import random

class ClassName():

    fix = 23

    def get_rand(self):
        self.__set_rand()
        return self.rand_int
    
    def __set_rand(self):
        self.rand_int = random.randint(1,20)


m = ClassName()
n = ClassName()
o = ClassName()

cn_lst = (ClassName(), ClassName(), ClassName())

for e in cn_lst:
    print(e, e.fix, e.get_rand())
