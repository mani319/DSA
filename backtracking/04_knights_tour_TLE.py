"""
"""

N = 8


def isSafe(board, row, col):
    if(row < 0 or row >= N):
        return False

    if(col < 0 or col >= N):
        return False

    if(board[row][col] != -1):
        return False

    return True


def knightsTourUtil(board, row_moves, col_moves, row, col, move):
    if(move == N*N):
        return True

    for i in range(0, 8):
        next_row = row + row_moves[i]
        next_col = col + col_moves[i]

        if(isSafe(board, next_row, next_col)):
            board[next_row][next_col] = move

            if(knightsTourUtil(board, row_moves, col_moves,
                               next_row, next_col, move+1)):
                return True

            board[next_row][next_col] = -1

    return False


def knightsTour():
    board = []
    for i in range(N):
        board += [[-1]*N]

    row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    row = 0
    col = 0
    move = 1
    board[0][0] = 0

    if(knightsTourUtil(board, row_moves, col_moves, row, col, move)):
        print("Sol Found:")
        for i in range(N):
            print(board[i])
    else:
        print("Knights Tour Ultra Faillllll")


if __name__ == "__main__":
    knightsTour()
