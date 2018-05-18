#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    '''
    prints a dictionary by ordered keys
    '''
    keys = sorted(list(my_dict))
    for key in keys:
        print('{}: {}'.format(key, my_dict[key]))
