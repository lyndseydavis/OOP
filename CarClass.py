class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    # def set_model(self, model):
    # self.__year_model = str(model)

    # def set_make (self, make):
    # self.__make = str(make)

    def get_model(self):
        return self.__year_model

    def get_year(self):
        return self.__make

    def get_speed(self):
        return self.__speed
