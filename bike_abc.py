

from abc import ABC, abstractmethod


class Bike(ABC):

    # __metaclass__ = abc.ABCMeta

    wheels = 2

    @classmethod
    def get_wheels(cls):
        return cls.wheels

    # Returns the type of bike (road, touring, mountain)
    @abstractmethod
    def get_type(self):
        return 
    
    @abstractmethod
    def get_color(self):
        return 

