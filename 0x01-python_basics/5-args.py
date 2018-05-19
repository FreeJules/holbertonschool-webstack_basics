#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    total_args = len(argv) - 1
    if total_args == 0:
        print('{} arguments.'.format(total_args))
    elif total_args == 1:
        print('{} argument:\n1: {}'.format(total_args, argv[total_args]))
    else:
        print('{} arguments:'.format(total_args))
        for arg in range(1, total_args + 1):
            print('{}: {}'.format(arg, argv[arg]))
