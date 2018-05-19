#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    enum = 0
    denom = 0
    for tupl in my_list:
        enum += tupl[0]*tupl[1]
        denom += tupl[1]
    return enum/denom
