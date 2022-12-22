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
        if isinstance(value, int):
            raise Exception(TypeError,f"{name} must be an integer")
        elif value <= 0:
            raise Exception(ValueError, f"{name} must be greater than 0")
