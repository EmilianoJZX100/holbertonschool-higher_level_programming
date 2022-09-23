#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size is not int:
            raise TypeError("size must be an integer")
