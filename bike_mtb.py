
from bike_abc import * 

class MountainBike(Bike):
    
    type = 'mountain'

    def __init__(self, value):
        self.color = value
        super().__init__()

    def get_type(self):
        return self.type
    
    def get_color(self):
        return self.color
    
    def set_color(self, value):
        self.color = value
