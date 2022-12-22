#!/usr/bin/python3
'''function that returns True
    if the object is an instance 
    of a specified class
'''


def is_same_class(obj, a_class):
    '''fucntion: is_same_class
        Returns Bool
        Args:
            obj (any): The object
            a_class (type)
    '''

    return True if isinstance(obj, a_class) else False
