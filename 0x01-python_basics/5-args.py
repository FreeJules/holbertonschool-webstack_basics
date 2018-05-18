#!/usr/bin/python3
import sys


total_args = len(sys.argv)
if __name__ == "__main__":
    if total_args == 1:
        print('0 arguments.')
    elif total_args == 2:
        print('1 argument:')
    else:
        print('{} arguments:'.format(total_args - 1))
    for arg in range(1, total_args):
        print ('{}: {}'.format(arg, sys.argv[arg]))
