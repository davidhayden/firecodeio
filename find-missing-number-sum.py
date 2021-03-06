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
    return sum(range(1,11)) - sum(list_numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
