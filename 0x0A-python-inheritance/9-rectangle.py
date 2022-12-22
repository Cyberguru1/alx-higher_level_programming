#!/usr/bin/python3
''' class rectangle inherted from baseGeometry
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''class: Rectangle inherited from baseGeometry
    '''

    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self,"width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        """ print"""
        return f"[Rectangle] {self.__width}/{self.__height}"
