"""
Write a function that takes in a string and
returns the reversed version of the string.
"""

def reverse_string(a_string):
    """
    Returns reversed version of string.

    >>> reverse_string('abcde')
    'edcba'
    >>> reverse_string('1')
    '1'
    >>> reverse_string('')
    ''
    >>> reverse_string('madam')
    'madam'
    """
    return a_string[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
