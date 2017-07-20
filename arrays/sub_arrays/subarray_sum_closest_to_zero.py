import math


def subarray_sum_closest_to_zero(arr):
    n = len(arr)

    prefix_sum = [[None, None]]*(n+1)
    prefix_sum[0] = [0, -1]
    for i in range(1, n+1):
        prefix_sum[i] = [prefix_sum[i-1][0] + arr[i-1], i-1]

    prefix_sum.sort()

    mini_diff = math.inf
    for i in range(1, n+1):
        curr_diff = prefix_sum[i][0] - prefix_sum[i-1][0]
        if(curr_diff < mini_diff):
            mini_diff = curr_diff
            start = prefix_sum[i-1][1] + 1
            end = prefix_sum[i][1]

    return start, end


if __name__ == "__main__":
    arrays = [[2, 3, -4, -1, 6],
              [2, -5, 4, -6, -3],
              [-1, 3, 2, -5, 4]]

    for array in arrays:
        print(array, "Subarray with min sum:", end=" ")
        print(subarray_sum_closest_to_zero(array))
