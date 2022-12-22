#!/usr/bin/python3
''' class rectangle inherted from baseGeometry
'''


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    '''class: Rectangle inherited from baseGeometry
    '''
    self.integer_balida

    
    def __init__(self, width, height) -> None:
        self.width = BaseGeometry.integer_validator(width)
        self.height = BaseGeom height
        super().__init__()
