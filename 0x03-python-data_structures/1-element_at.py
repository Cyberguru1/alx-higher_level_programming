#!/usr/bin/python3
def element_at(my_list, idx):
    """
    function that retreives an element
    form alist like c
    """
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
