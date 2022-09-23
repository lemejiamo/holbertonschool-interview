#!/usr/bin/env python3
"""
    Determine the fewest number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    coins: a list of coins available to meet a given amount
    total: amount to give
    return:  fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total == 0 or coins is None or coins == []:
        return -1

    my_coins = sorted(coins, reverse=True)
    money_left = total
    change = 0
    for coin in my_coins:
        while (money_left % coin >= 0 and money_left >= coin):
            change += int(money_left / coin)
            money_left = money_left % coin
    change = change if money_left == 0 else -1

    return change
