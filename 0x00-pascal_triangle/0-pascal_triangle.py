#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle up to a
specified number of rows.

The main function is:
    - pascal_triangle(n): Returns a list of lists representing the first n rows
      of Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
        list of lists of int: A list of lists, where each inner list represents
        a row in Pascal's Triangle. If n <= 0, returns an empty list.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Compute the values for the middle of the row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
