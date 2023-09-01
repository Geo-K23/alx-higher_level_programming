#!/usr/bin/python3
""" This python script finds a peak in alist of unsorted integers"""


def find_peak(list_of_integers):
    """This finds a peak in a list of unsorted integers"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
