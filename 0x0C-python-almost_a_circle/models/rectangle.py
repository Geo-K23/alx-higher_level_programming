#!/usr/bin/python3
"""
Class Module for a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new rectangle.

        args:
            width: width of rectangle
            height: height of rectangle
            x: int variable
            y: int variable
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        self.integer_validator_2('width', value)
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        self.integer_validator_2('height', value)
        self.__height = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """updates the Rectangle attributes"""
        if args:
            mylist = ['id', 'width', 'height', 'x', 'y']
            j = 0
            for arg in args:
                setattr(self, mylist[j], arg)
                j += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """prints rectangle to stdout using '#' character.
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """Returns the print() and str() representation of the Rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self.integer_validator_1('x', value)
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self.integer_validator_1('y', value)
        self.__y = value
