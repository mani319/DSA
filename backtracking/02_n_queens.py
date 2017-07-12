'''
The N Queen is the problem of placing N chess queens on an N×N chessboard
   so that no two queens attack each other.
'''

N = 8
print_all_solutions = False


def isSafe(board, row, col):
    # Check whether there is any queen in row
    for i in range(N):
        if(board[row][i] == 1):
            return False

    # Check whether there is any queen in column
    for i in range(N):
        if(board[i][col] == 1):
            return False

    # Check whether there is any queen in it's diagonals
    for i in range(N):
        if((row+col-i >= 0 and row+col-i < N and board[i][row+col-i]) or
           (i-row+col >= 0 and i-row+col < N and board[i][i-row+col])):
            return False

    return True


def NQueens_util(board, col):
    if(col == N):
        if(print_all_solutions is True):
            print("One possible solution is:")
            for row in range(N):
                print(board[row])
        return True

    for row in range(N):
        if(isSafe(board, row, col)):
            board[row][col] = 1

            # Go to next column and check
            if(print_all_solutions is True):
                NQueens_util(board, col+1)
            else:
                if(NQueens_util(board, col+1)):
                    return True

            board[row][col] = 0

    return False


def NQueens():
    board = []
    for row in range(N):
        board += [[0]*N]

    if(NQueens_util(board, 0)):
        print("The Placing of Queens is:")
        for row in range(N):
            print(board[row])
    else:
        print("Solution not found for %d Queens" % N)


if __name__ == "__main__":
    NQueens()
