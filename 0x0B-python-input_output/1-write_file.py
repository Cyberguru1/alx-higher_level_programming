#!/usr/bin/python3

'''
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''
        fucntion:
            write_file()
        Args:
            filename: file to write to
            text: text to write into the file
    '''
    with open(filename, 'w') as f:
        f.write(text)

    return len(text)
