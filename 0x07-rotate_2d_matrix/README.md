# Rotate 2D Matrix

## Description
This project contains a solution for rotating an n x n 2D matrix 90 degrees clockwise in-place.

## Function Prototype
```python
def rotate_2d_matrix(matrix):
```

## Requirements
* Python 3.8.10
* Ubuntu 20.04 LTS
* pycodestyle 2.8.0

## Usage
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
# Output: [[7, 4, 1],
#          [8, 5, 2],
#          [9, 6, 3]]
```

## Algorithm
The solution uses a two-step approach:
1. Transpose the matrix (swap elements across the main diagonal)
2. Reverse each row

This results in a 90-degree clockwise rotation of the original matrix.
