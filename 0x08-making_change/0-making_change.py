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
    current = 0
    used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        res = (total - current) // coin
        used += res
        if current == total:
            return used
    return -1
