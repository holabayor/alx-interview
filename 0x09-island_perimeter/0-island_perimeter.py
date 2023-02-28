#!/usr/bin/python3
'''
Given an island, return the perimeter of the island
'''


def island_perimeter(grid):
    ''' Calculate the perimeter of a given grid
        Returns the perimeter of the island
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # check if the current cell is an island (1)
                # check if the cell to the left is water (0)
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # add 1 to the perimeter

                # check if the cell above is water (0)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # add 1 to the perimeter

                # check if the cell to the right is water (0)
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # add 1 to the perimeter

                # check if the cell below is water (0)
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # add 1 to the perimeter

    return perimeter
