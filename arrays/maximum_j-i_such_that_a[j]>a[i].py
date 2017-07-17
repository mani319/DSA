'''

Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

Eg:
Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output: 6  (j = 7, i = 1)

Approach:http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

'''


def maximum_j_minus_i_such_that_aj_grtr_than_ai(arr):
    n = len(arr)

    # lMin[i] stores the minimum value from (arr[0], arr[1], ... arr[i])
    lMin = [0]*n
    lMin[0] = arr[0]
    for i in range(1, n):
        lMin[i] = min(arr[i], lMin[i-1])

    # rMax[j] stores the maximum value from (arr[j], arr[j+1], ..arr[n-1])
    rMax = [0]*n
    rMax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rMax[i] = max(arr[i], rMax[i+1])

    # Traverse both arrays from left to right to find optimum j - i
    i, j, max_diff = 0, 0, -1
    while(i < n and j < n):
        if(rMax[j] > lMin[i]):
            max_diff = max(j-i, max_diff)
            j += 1
        else:
            i += 1

    return max_diff


if __name__ == "__main__":
    arrays = [[34, 8, 10, 3, 2, 80, 30, 33, 1],
              [9, 2, 3, 4, 5, 6, 7, 8, 18, 0],
              [1, 2, 3, 4, 5, 6],
              [6, 5, 4, 3, 2, 1]]

    for array in arrays:
        print(array, "-->", maximum_j_minus_i_such_that_aj_grtr_than_ai(array))
