#!/usr/bin/python3
"""Square module"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """
        Initializes a square object.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
