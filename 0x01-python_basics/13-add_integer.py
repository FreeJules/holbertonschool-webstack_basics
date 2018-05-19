#!/usr/bin/python3
'''
a and b must be integers or floats or raise a TypeError exception
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
'''


def add_integer(a, b):
    '''
    adds 2 integers
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
