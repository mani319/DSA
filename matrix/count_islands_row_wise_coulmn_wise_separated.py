"""
Given a rectangular matrix which has only two possible values ‘X’ and ‘O’.
The values ‘X’ always appear in form of rectangular islands and
    these islands are always row-wise and column-wise separated
    by at least one line of ‘O’s.
Note that islands can only be diagonally adjacent.
Count the number of islands in the given matrix.

mat[M][N] =  {{'O', 'O', 'O'},
              {'X', 'X', 'O'},
              {'X', 'X', 'O'},
              {'O', 'O', 'X'},
              {'O', 'O', 'X'},
              {'X', 'X', 'O'}
             };
Output: Number of islands is 3
"""


def countIslands(mat, m, n):
    count = 0

    for i in range(m):
        for j in range(n):

            if(mat[i][j] == 'X'):
                if((i == 0 or mat[i-1][j] == 'O') and
                   (j == 0 or mat[i][j-1] == 'O')):
                    count += 1

    return count


if __name__ == "__main__":
    matrix = [['O', 'O', 'O'],
              ['X', 'X', 'O'],
              ['X', 'X', 'O'],
              ['O', 'O', 'X'],
              ['O', 'O', 'X'],
              ['X', 'X', 'O']]

    rows = len(matrix)
    cols = len(matrix[0])

    print(countIslands(matrix, rows, cols))
