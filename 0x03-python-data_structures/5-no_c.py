#!/usr/bin/python3
def no_c(my_string):
    """
    A function that returns a string without
    the alphabet c
    """
    return ''.join([var if var not in 'cC' else '' for var in my_string])
