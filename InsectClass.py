import random

class Insect:
    # The _ _init_ _ method initializes the

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    # calculate length of flight for each insect
    # randomly assign a value of 1 - 10 miles.

    def lenflight (self):
        self.flight == random.randint(1, 10)
    
    def get_flight (self):
        return self.flight