#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ 
    A function that returns a set
    of common elements in two
    sets 
    """
    new_list = list(map(lambda i : i in set_1 and i in set_2, set_1))
    return new_list
