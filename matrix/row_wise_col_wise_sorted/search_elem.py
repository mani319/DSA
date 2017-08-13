"""
Search Element in Row wise and Column wise sorted matrix
"""


def search(mat, m, n, x):
    i = 0
    j = n-1
    while(i < m and j >= 0):
        if(x == mat[i][j]):
            return True, i, j

        if(x < mat[i][j]):
            j -= 1
        else:
            i += 1

    return False


if __name__ == "__main__":
    matrix = [[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50],
              [96, 97, 98, 99]]

    m = len(matrix)
    n = len(matrix[0])
    elems = [29, 100, 1, 98, 96, 10, 34]
    for el in elems:
        print (search(matrix, m, n, el))
