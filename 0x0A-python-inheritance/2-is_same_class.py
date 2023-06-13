#!/usr/bin/python3
"""
This is a module of the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
    Returns:
        True if object is exactly an instance of the class, or False if not
    """
    return type(obj) == a_class
