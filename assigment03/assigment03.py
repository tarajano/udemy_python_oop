

class DoThis(dict):
    """docstring for DoThis"""
    def __init__(self):
        super(DoThis, self).__init__()

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

    def set_config(self):
        with open('dothis.config', 'w') as dtc:
            for (key, value) in self.items():
                dtc.write("{}={}\n".format(key, value))

    def print_config(self):
        with open('dothis.config', 'r') as dtc:
            for line in dtc.readlines():
                print(line)

    def load_config(self):
        with open('dothis.config', 'r') as dtc:
            for line in dtc.readlines():
                (key, value) = line.strip().split('=')
                if key:
                    self.__setitem__(key, value) 