#!/usr/bin/python3

'''
     a function that appends a string at the end of a text file
     (UTF8) and returns the number of characters added
'''

def append_write(filename="". text=""):
    '''
        function:
                append_write()
        Args:
            filename: file to write to
            text: text file to write too
        Returns:
                The number of charcters appended
    '''

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
