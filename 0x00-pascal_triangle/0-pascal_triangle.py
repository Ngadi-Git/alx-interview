#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(num):
    """Create a function def pascal_triangle(num): that returns a list of lists
    of integers representing the Pascal’s triangle of num
    """
    dbs = []
    if num > 0:
        for i in range(1, num + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            dbs.append(level)
    return res
