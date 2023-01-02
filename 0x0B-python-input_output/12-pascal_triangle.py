#!/usr/bin/python3
""" Implementation of pascal triangle"""


def pascal_triangle(n):
    """implements the pascal traingle
    Args:
        n (int): number of terms of pascal triangle
    """
    terms = []
    if n <= 0:
        return terms
    for i in range(n):
        term = []
        for j in range(i + 1):
            value = fact(i) // (fact(j)* fact(i - j))
            term.append(value)
        terms.append(term)
    return terms


def fact(n):
    """implements factorial
    Args:
        n(int) : number to find factorial
    Returns:
        returns the factorial
    """
    if n == 0:
        return 1
    return n * fact(n - 1)
