import typing
import collections

def isSudoku(board: list[list[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                return False
            
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])

    return True


def isValidSudoku(board):
    # Validate Rows
    for i in range(9):
        s =set()
        for j in range(9):
            item = board[i][j]
            if item in s:
                return False
            elif item != '.':
                s.add(item)

    # Validate Columns
    for i in range(9):
        s =set()
        for j in range(9):
            item = board[j][i]
            if item in s:
                return False
            elif item != '.':
                s.add(item)

    # Validate Boxes
    starts = [(0,0), (0,3), (0,6),
              (3,0), (3,3), (3,6),
              (6,0), (6,3), (6,6)]
    for i, j in starts:
        s =set()
        for row in range(i, i+3):
            for col in range(j, j+3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(isSudoku(board))