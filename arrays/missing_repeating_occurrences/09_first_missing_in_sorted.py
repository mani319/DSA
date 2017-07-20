"""
Given a sorted array of n distinct integers.
Each integer is in the range from 0 to m-1 and m > n.
Find the smallest number that is missing from the array.

Examples
Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
Output: 8
"""


def binary_search_method(arr, low, high):
    while(low <= high):
        if(low != arr[low]):
            return low

        mid = low + (high - low)//2

        if(mid == arr[mid]):
            low = mid + 1
        else:
            high = mid - 1

    return high+1


def firstElementMissing(arr):
    n = len(arr)

    print(binary_search_method(arr, 0, n-1))


if __name__ == "__main__":
    arrays = [[0, 1, 2, 3, 4, 5, 6, 7, 10],
              [0, 1, 2, 3],
              [4, 5, 10, 11],
              [0, 1, 2, 6, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 10],
              [0, 1, 3, 4, 5]]

    for array in arrays:
        print(array)
        firstElementMissing(array)
        print("-----------------------------------------------------------")
