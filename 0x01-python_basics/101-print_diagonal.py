#!/usr/bin/python3
def print_diagonal(n):
    if n > 0:
        for i in range(n):
            print('{}{}'.format(i*' ', '\\'))
    print()
