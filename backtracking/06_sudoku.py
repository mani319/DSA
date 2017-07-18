"""
"""

N = 9


def find_empty_row_col(grid, l):
    for row in range(0, N):
        for col in range(0, N):
            if(grid[row][col] == 0):
                l[0] = row
                l[1] = col
                return True

    return False


def isSafe(grid, row, col, val):
    for i in range(N):
        if(grid[row][i] == val):
            return False

    for i in range(N):
        if(grid[i][col] == val):
            return False

    for i in range(3):
        for j in range(3):
            if(grid[i+row-(row % 3)][j+col-(col % 3)] == val):
                return False

    return True


def solveSudoku(grid):
    l = [0, 0]
    if(not find_empty_row_col(grid, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if(isSafe(grid, row, col, num)):
            grid[row][col] = num

            if(solveSudoku(grid)):
                return True

            grid[row][col] = 0

    return False


if __name__ == "__main__":
    grid = []
    for i in range(N):
        grid += [[0]*N]

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if(solveSudoku(grid)):
        print("The solution for sudoku is: ")
        for i in range(N):
            print(grid[i])
    else:
        print("No Solution found")
