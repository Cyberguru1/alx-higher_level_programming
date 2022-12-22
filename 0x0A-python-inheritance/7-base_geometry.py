#!/usr/bin/python3
''' class of baseGeometry
'''


class BaseGeometry():
    '''class: BaseGeometry()
        args:
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type():
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
