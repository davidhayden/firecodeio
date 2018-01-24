"""
Write selection sort. The problem was unclear as to
do it in-place or return the value. I originally did
it in-place, which was apparently the wrong guess, so
I just returned the list I sorted in-place, even though
I realize one would not do both in a real situation.
"""


def selection_sort(a_list):
    """
    Returns a_list sorted using Selection Sort.

    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    >>> selection_sort([2, 1])
    [1, 2]
    >>> selection_sort([5, 4, 3, 2, 1, 0, -1, -2, -3 , -4])
    [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    """
    if a_list is None or len(a_list) < 2:
        return a_list

    for i in range(len(a_list) - 1):
        min_element = a_list[i]
        min_element_index = i

        for j in range(i + 1, len(a_list)):
            if a_list[j] < min_element:
                min_element = a_list[j]
                min_element_index = j

        a_list[i], a_list[min_element_index] = \
            a_list[min_element_index], a_list[i]

    return a_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
