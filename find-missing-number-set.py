"""
Given an list containing 9 numbers ranging
from 1 to 10, write a function to find the
missing number. Assume you have 9 numbers
between 1 to 10 and only one number is
missing.
"""


def find_missing_number(list_numbers):
    """
    Returns missing number.

    >>> find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10])
    3
    """
    all_numbers = set(range(1,11))
    partial_numbers = set(list_numbers)

    return all_numbers.difference(partial_numbers).pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
