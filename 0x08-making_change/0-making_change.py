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

    coins.sort(reverse=True)
    num_coins = 0
    coins_total = total
    for coin in coins:
        if coins_total <= 0:
            break
        if coin <= coins_total:
            num_coins += coins_total // coin
            coins_total %= coin
    if coins_total == 0:
        return num_coins
    else:
        return -1
