#!/usr/bin/env python3
"""
    Determine the fewest number of coins needed to meet a given amount
"""
import sys


def makeChange(coins, total):
    """
    coins: a list of coins available to meet a given amount
    total: amount to give
    return:  fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    # initial state of number of coins to return
    res = -1
    if total == 0 or coins is None or coins == []:
        return res
    # Initialize result
    m = len(coins)
    # Try every coin that has smaller value than Total
    for i in range(0, m):
        if (coins[i] <= total):
            sub_res = makeChange(coins, total - coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

    return res
