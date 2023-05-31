#!/usr/bin/python3
"""Square module"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position:  position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the coordinates of this Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        self.__position = value

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
        if self.__size == 0:
            print()
        else:
            k = 0
            pos1, pos2 = self.__position
            for new_line in range(pos2):
                print()
            while k < self.__size:

                j = 0
                while j < pos1:
                    print(" ", end='')
                    j += 1

                num = 0
                while num < self.__size:
                    print("{}".format("#"), end='')
                    num += 1
                print()
                k += 1
