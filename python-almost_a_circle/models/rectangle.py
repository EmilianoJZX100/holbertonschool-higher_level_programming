#!/usr/bin/python3
"""inherits from base"""


class Rectangle(Base):
    """class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
