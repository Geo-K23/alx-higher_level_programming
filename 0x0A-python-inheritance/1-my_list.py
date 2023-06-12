#!/usr/bin/python3
"""
Contains MyList class that inherits class list
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
