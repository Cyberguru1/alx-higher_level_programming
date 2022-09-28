#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    A function that returns a set
    of common elements in two
    sets
    """
    f = lambda i :  i in set_2 
    new_list = list(filter(f, set_1))
    return new_list
