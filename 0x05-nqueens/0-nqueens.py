#!/usr/bin/python3
"""
N Queens
"""
import sys
from typing import List  # For annotations

boardcnt = 0
solution = []


def IsBoardOk(chessboard: List, row: int, col: int):
    # Check if there is a queen 'Q' positioned to
    # the left of column on the same row.
    for c in range(col):
        if (chessboard[row][c] == 'Q'):
            return False

    # Check if there is queen 'Q' positioned on the upper left diagonal
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if (chessboard[r][c] == 'Q'):
            return False

    # Check if there is queen 'Q' positioned on the lower left diagonal
    for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)):
        if (chessboard[r][c] == 'Q'):
            return False

    return True


def PlaceNQueens(chessboard: List, col: int):
    # If all the columns have a queen 'Q', a solution has been found.
    global boardcnt
    if (col >= len(chessboard)):
        boardcnt += 1
        print(solution)
    else:
        # Else try placing the queen on each row of the column
        # and check if the chessboard remains OK.
        for row in range(len(chessboard)):
            chessboard[row][col] = 'Q'
            solution.append([row, col])
            if IsBoardOk(chessboard, row, col):
                # Chess board was OK, hence try placing the
                # queen 'Q' in the next column.
                PlaceNQueens(chessboard, col + 1)

            # As previously placed queen was not valid, restore '.'
            chessboard[row][col] = '.'
            solution.remove([row, col])


def main(N):
    chessboard = []
    for i in range(N):
        row = ["."] * N
        chessboard.append(row)

    # Start placing the queen 'Q' from the 0'th column.
    PlaceNQueens(chessboard, 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        main(n)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
