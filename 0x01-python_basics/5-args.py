#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    total_args = len(argv)
    if total_args == 1:
        print('0 arguments.')
    elif total_args == 2:
        print('1 argument:\n1: {}'.format(argv[1]))
    else:
        print('{} arguments:'.format(total_args - 1))
        for arg in range(1, total_args):
            print ('{}: {}'.format(arg, argv[arg]))
