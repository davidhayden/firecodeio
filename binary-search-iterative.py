"""
Write a function that searches a list of ints for
a given integer using the Binary Search Algorithm.
"""


def binary_search(a_list, item):
    """
    Return True if item in a_list
    otherwise False.

    params:
        a_list: lst, list of int in sorted order
        item: int, item to find in a_list

    returns:
        bool: True if item in a_list, otherwise False

    >>> binary_search([2, 5, 7, 8, 9], 9)
    True
    >>> binary_search([2, 8, 9, 12], 6)
    False
    >>> binary_search([2], 4)
    False
    >>> binary_search([], 9)
    False
    """
    if a_list == None or len(a_list) == 0:
        return False

    left_index = 0
    right_index = len(a_list) - 1

    while left_index <= right_index:
        midpoint = (left_index + right_index) // 2

        if a_list[midpoint] == item:
            return True

        if a_list[midpoint] < item:
            left_index = midpoint + 1
        else:
            right_index = midpoint - 1
    
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
