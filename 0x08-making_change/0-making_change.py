#!/usr/bin/python3
"""
making change
"""


def make_change(coins, total):
    """
    coins and total
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    
    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total %= coin
    
    if total > 0:
        return -1
    return num_coins