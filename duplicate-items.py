"""
Write a function - duplicate_items to find the
redundant or repeated items in a list and return
them in sorted order.

This method should return a list of redundant
integers in ascending sorted order (as
illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]
"""


from collections import Counter

def duplicate_items(list_numbers):
    counts = Counter(list_numbers)

    items = [n[0] for n in counts.items() if n[1] > 1]

    return sorted(items)
