#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where:
            - 0 represents water
            - 1 represents land
            - Each cell is square, with a side length of 1
            - Cells are connected horizontally/vertically (not diagonally)

    Returns:
        int: The perimeter of the island
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 sides of the current land cell
                # Add 1 to perimeter for each adjacent water cell or border

                # Check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
