#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    funtion that prints out he content of
    a list to a string
    """
    for val in my_list:
        print('{:d}'.format(val))