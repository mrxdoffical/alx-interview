#!/usr/bin/python3
"""
Module for making change using the minimum number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    Args:
        coins: list of coin values
        total: target amount
    Returns:
        Fewest number of coins needed to meet total, -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Initialize dp array with total + 1 (impossible value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill dp array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
