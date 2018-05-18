#!/usr/bin/python3
def no_c(str):
    new_str = ''
    for char in str:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
