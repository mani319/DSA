"""
Given a matrix of n*n size, print its elements in diagonally zig-zag pattern

Input : mat[3][3] = {{1, 2, 3},
                     {4, 5, 6},
                     {7, 8, 9}}

Output : 1 2 4 7 5 3 6 8 9
"""


def printDiagonallyZigZag(mat, n):
    i, j = 0, 0

    isUp = True

    k = 0
    while(k < n*n):
        if(isUp):
            while(i >= 0 and j < n):
                print(mat[i][j], end=" ")
                i -= 1
                j += 1
                k += 1

            if(i < 0 and j < n):
                i = 0

            if(j == n):
                i += 2
                j -= 1
            print()

        else:
            while(j >= 0 and i < n):
                print(mat[i][j], end=" ")
                j -= 1
                i += 1
                k += 1

            if(j < 0 and i < n):
                j = 0

            if(i == n):
                j += 2
                i -= 1
            print()

        isUp = not isUp


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rows = len(matrix)

    printDiagonallyZigZag(matrix, rows)
