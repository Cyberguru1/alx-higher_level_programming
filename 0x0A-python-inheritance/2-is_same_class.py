#!/usr/bin/python3
'''function that returns True
    if the object is an instance 
    of a specified class
'''


def is_same_class(obj, a_class):
    '''fucntion: is_same_class
        Returns Bool
    '''

    return True if isinstance(a_class, obj) else False
