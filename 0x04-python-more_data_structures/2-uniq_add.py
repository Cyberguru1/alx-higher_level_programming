#!/usr/bin/python3
def uniq_add(my_list=[]):

    """
    A function that adds up unique element in a list
    """
    unique =  set(my_list)
    summed = unique[0]

    for i in unique[1:]:
        summed += i

    return (summed)
