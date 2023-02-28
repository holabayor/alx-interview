#!/usr/bin/python3
'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise
'''


from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ Determine the fewest number of coins needed to
        meet a given i total
    Args:
        coins (list): List of integers
        total (int): Total number of coins
    Return:
        Fewest number of coins needed to meet total else -1
    """
    totalList = [total + 1] * (total + 1)
    totalList[0] = 0
    for i in range(1, total + 1):
        # print(f'This is loop no {i}')
        for coin in coins:
            if i - coin >= 0:
                totalList[i] = min(
                    totalList[i], 1 + totalList[i - coin])
                # print(f'The list is {totalList}')

    return totalList[total] if totalList[total] != total + 1 else -1
