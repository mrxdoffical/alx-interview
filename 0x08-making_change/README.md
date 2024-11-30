# Making Change

## Description
This project contains a solution to determine the fewest number of coins needed to meet a given amount total from a pile of coins of different values.

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
* All files should end with a new line
* The first line of all files should be exactly #!/usr/bin/python3
* A README.md file at the root of the project folder is mandatory
* Code should use the PEP 8 style (version 1.7.x)
* All files must be executable

## Task: Change comes from within
Write a function that determines the fewest number of coins needed to meet a given amount total.

### Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
* coins: a list of the values of the coins in your possession
* total: the target amount to make change for

### Returns
* Fewest number of coins needed to meet total
* If total is 0 or less, return 0
* If total cannot be met by any number of coins you have, return -1

### Constraints
* The value of a coin will always be an integer greater than 0
* You can assume you have an infinite number of each denomination of coin in the list

### Example
```python
makeChange([1, 2, 25], 37)  # Returns: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Returns: -1
```
