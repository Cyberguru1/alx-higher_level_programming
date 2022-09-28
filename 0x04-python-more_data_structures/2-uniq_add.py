#!/usr/bin/python3
def uniq_add(my_list=[]):

    """
    A function that adds up unique element in a list
    """
    summed =  sum(set(my_list))
    return (summed)