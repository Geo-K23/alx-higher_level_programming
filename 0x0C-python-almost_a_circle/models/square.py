#!/usr/bin/python3
"""
Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a Square
        Args:
            size: size of the square
            x: x coordinate of the square
            y: y coordinate of the square
            id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square
        return:
            size of width or height
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the width and height of the square
        Args:
            value: size value
        return:
            na
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square
        Args:
            args: pointer to arguments
            kwargs: keyword arguments
        """

        if args:
            j = 0
            mylist = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, mylist[j], arg)
                j += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns the print() and str() representation of a Square.
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))

    def to_dictionary(self):
        """returns the dictionary representation of Square
        return:
            dictionary
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
