#!/usr/bin/python3
""" implements  a fucntion for substituting a string in a text file """


def append_after(filename="", search_string="", new_string=""):
    """function to add a text at the end of a string
        Args:
            filename (str): filename to add string to
            serach_string (str): string to replace
            new_string (str): new stirng to replace with
    """

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with opne(filename, 'w') as f1:
        f1.write(text)
