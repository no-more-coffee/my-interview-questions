from functools import reduce
from typing import List


def getSquareDigits(board, k, l):
    for i in range(3 * k, 3 * k + 3):
        for j in range(3 * l, 3 * l + 3):
            cell = board[i][j]
            if cell != '.':
                yield cell

reduce()
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            digits = [d for d in row if d != '.']
            if len(digits) != len(set(digits)):
                return False

        for i in range(9):
            digits = [row[i] for row in board if row[i] != '.']
            if len(digits) != len(set(digits)):
                return False

        for k in range(3):
            for l in range(3):
                digits = list(getSquareDigits(board, k, l) or ())
                if len(digits) != len(set(digits)):
                    return False

        return True
