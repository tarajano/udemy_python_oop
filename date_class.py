
import datetime


class Date(object):
    
    def get_date(self):
        return datetime.datetime.today().strftime('%Y-%m-%d')

        