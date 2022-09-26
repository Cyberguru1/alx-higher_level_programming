#!/usr/bin/python3
def multiple_returns(sentence):
    """
    This function returns a tuple with
    the length of a string
    as its first character
    """
    first = None if len(sentence) == 0 else sentence[0]
    length = len(sentence)
    return length, first

