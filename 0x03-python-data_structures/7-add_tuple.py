#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function that adds up
    two tuples
    """
    arg1 = 0 if len(tuple_a) == 1 else tuple_a[1]
    arg2 = 0 if len(tuple_b) == 1 else tuple_b[1]
    firs_arg = tuple_a[0] + tuple_b[0]
    sec_arg = arg1 + arg2
    return (firs_arg, sec_arg)
