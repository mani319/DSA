"""
Print a given matrix in spiral form

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
"""


def printSpiral(mat, m, n):
    # starting row and starting column
    r, c = 0, 0

    while(r < m and c < n):
        # print upper most row
        for i in range(c, n):
            print(mat[r][i], end=" ")
        r += 1

        # print right most column
        for i in range(r, m):
            print(mat[i][n-1], end=" ")
        n -= 1

        # print lower most row if exists
        if(r < m):
            for i in range(n-1, c-1, -1):
                print(mat[m-1][i], end=" ")
            m -= 1

        # print left most column if exists
        if(c < n):
            for i in range(m-1, r-1, -1):
                print(mat[i][c], end=" ")
            c += 1


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18]]

    rows = len(matrix)
    cols = len(matrix[0])

    printSpiral(matrix, rows, cols)
