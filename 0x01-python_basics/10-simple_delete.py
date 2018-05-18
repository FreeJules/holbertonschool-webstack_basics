#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    '''
    deletes a key in a dictionary
    '''
    my_dict.pop(key, None)
    return my_dict
