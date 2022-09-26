#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    a function that returns modified version
    of a copied list
    """
    copy_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
