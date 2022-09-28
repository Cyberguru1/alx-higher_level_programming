#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ 
    A function that returns a set
    of common elements in two
    sets 
    """
    new_list = [i if i in set_1 and i in set_2 for i in set_1]
    return new_list

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))