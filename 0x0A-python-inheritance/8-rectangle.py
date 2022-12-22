#!/usr/bin/python3
''' class rectangle inherted from baseGeometry
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    '''class: Rectangle inherited from baseGeometry
    '''

    
    def __init__(self, width, height) -> None:
        self.width = self.integer_validator(width)
        self.height = self.integer_validator(height)
