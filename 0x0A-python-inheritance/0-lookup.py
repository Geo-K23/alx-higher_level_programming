#!/usr/bin/python3
"""
This is the lookup function
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object

    Args:
        The object to inspect
    Returns:
        A sorted list of attributes and method names
    """
    return dir(obj)
