#!/usr/bin/python3
''' class rectangle inherted from baseGeometry
'''


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    '''class: Rectangle inherited from baseGeometry
    '''

    
    def __init__(self, width, height) -> None:
        self.width = Baseinteger_validator(width)
        self.height = height
        super().__init__()
