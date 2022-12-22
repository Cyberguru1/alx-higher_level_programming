#!/usr/bin/python3
''' function that returns the JSON representation of an object (string)
'''

import json


def from_json_string(my_obj):
    ''' module to_json_strin
     returns JSON representation
    '''
    return json.loads(my_obj)
