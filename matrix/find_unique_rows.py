"""
Given a binary matrix, print all unique rows of the given matrix.

Input:
{0, 1, 0, 0, 1}
{1, 0, 1, 1, 0}
{0, 1, 0, 0, 1}
{1, 1, 1, 0, 0}
Output:
0 1 0 0 1
1 0 1 1 0
1 1 1 0 0
"""


def printUniqueRows(mat, m, n):
    hash_map = {}

    for i in range(m):
        row = ""
        for j in range(n):
            row += str(mat[i][j])

        if(row not in hash_map.keys()):
            for ch in range(len(row)):
                print(int(row[ch]), end=" ")
            print()
            hash_map[row] = True


if __name__ == "__main__":
    matrix = [[0, 1, 0, 0, 1],
              [1, 0, 1, 1, 0],
              [0, 1, 0, 0, 1],
              [1, 0, 1, 0, 0],
              [1, 0, 1, 1, 0]]

    rows = len(matrix)
    cols = len(matrix[0])

    printUniqueRows(matrix, rows, cols)
