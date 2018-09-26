
class InstanceCounter(object):
    """docstring for InstanceCounter"""
    count = 0

    def __init__(self, arg):
        super(InstanceCounter, self).__init__()
        self.value = arg
        InstanceCounter.count += 1

    def get_value():
        return self.value

    def set_value(self, arg):
        self.value = arg

ic_lst = [InstanceCounter(x) for x in range(2, 10, 2)]

for i in ic_lst:
    print(i, i.count, i.value)