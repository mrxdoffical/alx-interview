#!/usr/bin/python3
"""
This module contains functions to calculate the minimum operations needed
to achieve a given number of characters using "Copy All" and "Paste".
"""


def prime_factors(n):
    """
    Calculate the prime factors of a given number.

    Args:
        n (int): The number to calculate prime factors for.

    Returns:
        List[int]: A list of prime factors of the number.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The number of characters to achieve.

    Returns:
        int: The minimum number of operations needed. If n is impossible
        to achieve, returns 0.
    """
    if n < 2:
        return 0
    factors = prime_factors(n)
    return sum(factors)
