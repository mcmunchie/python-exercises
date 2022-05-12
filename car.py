'''
Object-oriented programming practice in Python
'''
class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def set_make(self, make):  # mutator method (aka getter, setter)
        self.__make = make

    def __str__(self,): # \ is continuation character, alt to ()
        return "The year model is " + self.__year_model + ", make is " \
            + self.__make + ", current speed is " + str(self.__speed)
