
import os

class ConfigDict(dict):
    """docstring for ConfigDict"""
    config_file = None

    def __init__(self, filename):
        super(ConfigDict, self).__init__()
        self.config_file = filename
        self._load_config()

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self._write_config_file()
    
    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

    def __test_file_access(self, mode):
        # mode: 'r', 'w'
        try:
            with open(self.config_file, mode) as dtc:
                pass
        except IOError as err:
            print('ERROR: {0}'.format(str(err)))
            exit()

    def _write_config_file(self):
        self.__test_file_access('w')
        with open(self.config_file, 'w') as dtc:
            for (key, value) in self.items():
                dtc.write("{0}={1}\n".format(key, value))

    def print_config_file(self):
        self.__test_file_access('r')
        with open(self.config_file, 'r') as dtc:
            for line in dtc.readlines():
                print(line.strip())
    
    def print_dict(self):
        for (key, value) in self.items():
            print("{0} -> {1}".format(key, value))

    def _load_config(self):
        self.__test_file_access('r')
        with open(self.config_file, 'r') as dtc:
            for line in dtc.readlines():
                (key, value) = line.strip().split('=', 1)
                if key:
                    self.__setitem__(key, value)


class ConfigKeyError(Exception):
    """docstring for ConfigKeyError"ConfigDict, """
    def __init__(self, *args):
        # super(ConfigKeyError, ConfigDict,  self).__init__()
        self.good_keys = list(args[0].keys())
        self.bad_key = args[1]

    def __str__(self):
         return 'Key "{}" is not present in dictionary.\nAvailable keys are: {}'.format(self.bad_key, ' '.join(self.good_keys))









        