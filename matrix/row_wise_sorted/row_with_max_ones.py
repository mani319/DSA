"""
Given a boolean 2D array, where each row is sorted.
Find the row with the maximum number of 1s.

Example
Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2
"""


def firstOne(arr, low, high):
    while(low <= high):
        mid = low + (high - low) // 2

        if(arr[mid] == 1 and (mid == 0 or arr[mid-1] == 0)):
            return mid
        elif(arr[mid] == 1):
            high = mid - 1
        else:
            low = mid + 1

    return -1


def row_with_max_ones(mat, m, n):
    row_index = 0
    j = firstOne(mat[0], 0, len(mat[0])-1)
    if(j == -1):
        j = n - 1

    for i in range(1, m):
        while(j >= 0 and mat[i][j] == 1):
            j = j - 1
            row_index = i

    return row_index


if __name__ == "__main__":
    matrix = [[0, 0, 0, 0],
              [0, 1, 1, 1],
              [0, 0, 1, 1],
              [1, 1, 1, 1],
              [0, 0, 0, 0]]
    rows = len(matrix)
    cols = len(matrix[0])
    print (row_with_max_ones(matrix, rows, cols))
