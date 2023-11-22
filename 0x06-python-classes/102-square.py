#!/usr/bin/python3
"""Square class defination"""


class Square:
    """square body"""

    def __init__(self, siz=0):
        """square contructor
        Args: size: length of a side of Square
        """
        self.__siz = siz

    @property
    def size(self):
        """"The propery of size as the length
        of a side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__siz

    @size.setter
    def size(self, values):
        if not isinstance(values, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__siz = values

    def area(self):
        """Get the area instance to comparators"""
        return self.__siz * self.__siz

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
