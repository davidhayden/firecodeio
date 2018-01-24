"""
You are given an m x n 2D image matrix (List of Lists) where
each integer represents a pixel. Flip it in-place along its
horizontal axis.

Example:

Input image :
              1 1
              0 0
Modified to :
              0 0
              1 1

"""


def flip_horizontal_axis(matrix):
    """Returns a list of lists in reverse order."""
    matrix.reverse()


if __name__ == '__main__':
    a = [[1, 1], [0, 0]]
    flip_horizontal_axis(a)
    assert(a == [[0, 0], [1, 1]])
