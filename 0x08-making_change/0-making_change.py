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
    if coins == [] or coins is None:
        return -1
    try:
        s = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    num_coins = 0

    for c in coins:
        if total % c == 0:
            num_coins += int(total / c)
            return num_coins

        if total - c >= 0:
            if int(total / c) > 1:
                num_coins += int(total / c)
                total = total % c
            else:
                num_coins += 1
                total -= c
                if total == 0:
                    break
    if total > 0:
        return -1
    return num_coins
