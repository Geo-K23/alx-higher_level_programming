#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A class that defines a square

    Attributes:
        __size (int): The size of the square (private attribute).
    """
    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size(int): The size of the square.
        """
        self.__size = size
