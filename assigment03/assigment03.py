

class ConfigDict(dict):
    """docstring for ConfigDict"""
    def __init__(self):
        super(ConfigDict, self).__init__()
        self._load_config()

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self._write_config_file()

    def _write_config_file(self):
        with open('dothis.config', 'w') as dtc:
            for (key, value) in self.items():
                dtc.write("{}={}\n".format(key, value))

    def print_config_file(self):
        with open('dothis.config', 'r') as dtc:
            for line in dtc.readlines():
                print(line.strip())
    
    def print_dict(self):
        for (key, value) in self.items():
            print("{} -> {}".format(key, value))

    def _load_config(self):
        with open('dothis.config', 'r') as dtc:
            for line in dtc.readlines():
                (key, value) = line.strip().split('=')
                if key:
                    self.__setitem__(key, value) 