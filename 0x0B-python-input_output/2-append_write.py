#!/usr/bin/python3
"""Defines a function for file-appending"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename: The name of the file to append to.
        text: The string to append to the file.
    Return:
        The number of characters added to file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
