#!/usr/bin/python3
'''
Given an island, return the perimeter of the island
'''


from typing import List

def island_perimeter(grid: List[List[int]]) -> int:
    ''' Calculate the perimeter of a given grid
        Returns the perimeter of the island
    '''
    for i in grid:
        for j in grid[i]:
            print(grid[i][j])
    return i * j