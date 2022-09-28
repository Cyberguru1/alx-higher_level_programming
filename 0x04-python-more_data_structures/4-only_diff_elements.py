#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """"
    A function that stores 
    an element that is different
    between two sets
    """
    f = lambda i :  i not in set_2 
    new_list = list(filter(f, set_1))
    return new_list
