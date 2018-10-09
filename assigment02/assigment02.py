import datetime


class WriteFile(object):
    """docstring for WriteFile"""
    def __init__(self, arg):
        self.filename = arg
        self.__create_filehandle__()

    def __create_filehandle__(self):
        self.filehandle = open(self.get_filename(), 'w')

    def get_filename(self):
        return self.filename

    def get_filehandle(self):
        return self.filehandle


class DelimFile(WriteFile):
    """docstring for DelimFile"""
    def __init__(self, file, delim):
        super(DelimFile, self).__init__(file)
        self.delimiter = delim

    def write(self, text):
        text = text.replace(' ', self.delimiter)
        self.filehandle.write("{}\n".format(text))


class LogFile(WriteFile):
    """docstring for LogFile"""
    def __init__(self, arg):
        super(LogFile, self).__init__(arg)

    def  write(self, text):
        self.filehandle.write("{} - {}\n".format(str(datetime.datetime.now()), str(text)))
        