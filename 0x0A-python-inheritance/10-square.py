#!/usr/bin/python3
'''
    class square that inherits from Rectangle(8-rectangle)
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''class: Square
        Args:
            size: input size
    '''

    def __init__(self, size):
        self.__size = size
        Base.integer_validator(self, "size", size)

    def area(self):
        return self.__size*self.__size
