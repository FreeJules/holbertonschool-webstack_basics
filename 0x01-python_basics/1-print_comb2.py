#!/usr/bin/python3
print('{}'.format(', '.join([str(i).zfill(2) for i in range(0, 99)])), end='')
print(', {}'.format(99))
