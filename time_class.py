

import datetime
from date_class import Date


class Time(Date):

    def get_time(self):
        return datetime.datetime.today().strftime('%H:%M:%S')
    
    def print_me(self):
        print(self.get_date() + ' ' + self.get_time())
