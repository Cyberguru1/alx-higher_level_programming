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
        if isinstance(int, value):
            raise Exception(TypeError,"name must be an integer")
        elif 