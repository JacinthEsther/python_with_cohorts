import collections


# from _ast import List


# Determine if a 9 x 9 sudoku board is valid.
# Only the filled cells need to be validated according to the rules
# 1. each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition


# t = [ [0]*3 for i in range(3)]


def is_valid_sudoku(board: list[list[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == "." or board[r][c] == "" or board[r][c] == " ":
                continue
            if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True


class Solution:
    pass


print(is_valid_sudoku([["1", "2", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
