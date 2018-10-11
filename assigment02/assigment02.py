import datetime
from abc import ABC

class WriteFile(ABC):
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

    def write(self):
        return


class DelimFile(WriteFile):
    """docstring for DelimFile"""
    def __init__(self, file, delim):
        super(DelimFile, self).__init__(file)
        self.delimiter = delim

    def write(self, text):
        text = self.__wrap_delimiter(text)
        text = text.replace(' ', self.delimiter)
        self.filehandle.write("{}\n".format(text))

    def __wrap_delimiter(self, arg_text):
        # if current delimiter is present in input text,
        # then wrap it with double quotes.
        # simple split by (hard-coded) single space 
        text_lst = list()
        for word in arg_text.split(' '):
            if self.delimiter not in word:
                text_lst.append(word)
            else:
                text_lst.append("\"{}\"".format(word))

        return ' '.join(map(str, text_lst))


class LogFile(WriteFile):
    """docstring for LogFile"""
    def __init__(self, arg):
        super(LogFile, self).__init__(arg)

    def  write(self, text):
        self.filehandle.write("{} - {}\n".format(str(datetime.datetime.now()), str(text)))
        