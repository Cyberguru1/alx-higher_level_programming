#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    A function that replaces all
    occurrences of an element by another in
    a new list.
    """
    new_list = my_list.copy()
    new_list[new_list.index(search)] = replace
    return new_list
