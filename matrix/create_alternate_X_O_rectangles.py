"""
Create a matrix of size m x n in which every elements is either X or 0.
The Xs and 0s must be filled alternatively,
    the matrix should have outermost rectangle of Xs,
    then a rectangle of 0s,
    then a rectangle of Xs, and so on

Input:  m = 6, n = 7
Output: Following matrix
X X X X X X X
X 0 0 0 0 0 X
X 0 X X X 0 X
X 0 X X X 0 X
X 0 0 0 0 0 X
X X X X X X X
"""


def createAlternateXO(m, n):
    mat = []
    for i in range(m):
        mat += [[0]*n]

    r, c = 0, 0
    char = 'X'
    while(r < m and c < n):
        for i in range(c, n):
            mat[r][i] = char
        r += 1

        for i in range(r, m):
            mat[i][n-1] = char
        n -= 1

        if(r < m):
            for i in range(n-1, c-1, -1):
                mat[m-1][i] = char
            m -= 1

        if(c < n):
            for i in range(m-1, r-1, -1):
                mat[i][c] = char
            c += 1

        if(char == 'X'):
            char = 'O'
        else:
            char = 'X'

    return mat


if __name__ == "__main__":
    rows = 6
    cols = 7

    matrix = createAlternateXO(rows, cols)

    for i in range(len(matrix)):
        print(matrix[i])
