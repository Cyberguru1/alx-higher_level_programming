#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    a function that prints out all the 
    integers of a list in reverse order
    """
    if my_list == []:
        return
        
    my_list1 = my_list[::-1]
    for i in range(len(my_list)):
        print("{:d}".format(my_list1[i]))
