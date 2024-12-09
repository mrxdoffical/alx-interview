# Island Perimeter

This project contains a Python function that calculates the perimeter of an island in a grid. The grid is represented as a 2D array where 0 represents water and 1 represents land.

## Problem Description

Given a grid where:
- 0 represents water
- 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, width and height don't exceed 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

The task is to calculate the perimeter of the island.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- Allowed editors: vi, vim, emacs
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use PEP 8 style (version 1.7)
- All modules and functions must be documented
- All files must be executable

## File Structure

- `0-island_perimeter.py`: Contains the implementation of the island_perimeter function
- `0-main.py`: Main file for testing the implementation

## Function Description

```python
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
        grid (List[List[int]]): 2D list of integers representing the island
    
    Returns:
        int: The perimeter of the island
    """
```

## Example Usage

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Algorithm

The function works by:
1. Iterating through each cell in the grid
2. When a land cell (1) is found:
   - Checks all four adjacent sides
   - Adds 1 to the perimeter for each side that is either:
     * A grid border
     * Adjacent to a water cell (0)

## Time Complexity

- Time Complexity: O(rows × cols) where rows and cols are the dimensions of the grid
- Space Complexity: O(1) as we only use a constant amount of extra space
