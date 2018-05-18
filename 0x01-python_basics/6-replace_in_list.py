#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    replaces an element of a list at a specific position
    '''
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
    return my_list
