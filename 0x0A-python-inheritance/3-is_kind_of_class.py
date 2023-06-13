#!/usr/python3
"""
This contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
    Return:
        True if object is an instance or inherited the class, else False
    """
    return isinstance(obj, a_class)
