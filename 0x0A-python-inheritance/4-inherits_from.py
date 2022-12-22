#!/usr/bin/python3
'''function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
'''


def inherits_from(obj, a_class):
    '''
        function: inherits_from(obj, a_class)

        Args:
            obj: object attribute to check
            a_class: the class to compare with
        Returns:
            returns boolean
    '''

    return  type(obj) != a_class and isinstance(obj, a_class)
