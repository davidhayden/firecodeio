"""
Given a string as the input, append characters
to it to make it into a palindrome. Return this
new palindrome.

Note: If the input is a palindrome then it
should be returned as is.
"""


def make_palindrome(input):
    """
    Returns a palindrome by appending
    characters to input.
    
    params:
        input: str
        
    return:
        str
        
    >>> make_palindrome('race')
    'racecar'
    >>> make_palindrome('abc')
    'abcba'
    >>> make_palindrome('madam')
    'madam'
    >>> make_palindrome('rad')
    'radar'
    >>> make_palindrome('aba')
    'aba'
    """
    if input == input[::-1]:
        return input
        
    return input + input[-2::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
