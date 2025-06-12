#!/usr/bin/python3
"""Module for makeChange function"""


def makeChange(coins, total):
    """
    Determines the fewest numner of coins needed to meet total,
    given coins of different values
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    return dp[total]
