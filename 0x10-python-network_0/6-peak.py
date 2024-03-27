#!/usr/bin/python3
"""Algorithms for list of integers."""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    peak = list_of_integer[0]
    for num in list_of_integers[1:]:
        if num > peak:
            peak = num
    return peak

