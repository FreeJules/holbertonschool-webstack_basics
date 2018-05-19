#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (len(position) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(position[0], int) or
        not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or
        not isinstance(value[0], int) or not isinstance(value[1], int) or
        value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''
        returns the current square area
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size + self.__position[1]):
                if i < self.__position[1]:
                    print()
                    continue
                for j in range(0, self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(' ', end='')
                        continue
                    print('#', end='')
                print()
