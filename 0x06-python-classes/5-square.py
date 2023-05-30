#!/usr/bin/python3
"""Square module"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """
        Initializes a square object.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square (getter).

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' to stdout.

        If the size of the square is 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
