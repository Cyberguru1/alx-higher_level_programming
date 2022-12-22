#!/usr/bin/python3

'''
    a function that reads a text file (UTF8) 
    and prints it to stdout
'''


def read_file(filename=""):
    '''function: read_file()
        Args:
            filename: file to read from
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(),end='')
