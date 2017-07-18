"""
Given a 2D matrix, print all elements of the given matrix in diagonal order.

Input:
    1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   17    18    19    20

Output:
    1
    5     2
    9     6     3
   13    10     7     4
   17    14    11     8
   18    15    12
   19    16
   20

"""


def printDiagonally(mat, m, n):
    r, c = 0, 0

    for k in range(m):
        i = k
        j = 0
        while(i >= 0 and j < n):
            print(mat[i][j], end=" ")
            i -= 1
            j += 1
        print()

    for k in range(1, n):
        i = m-1
        j = k
        while(i >= 0 and j < n):
            print(mat[i][j], end=" ")
            i -= 1
            j += 1
        print()


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
              [17, 18, 19, 20]]

    rows = len(matrix)
    cols = len(matrix[0])

    printDiagonally(matrix, rows, cols)
