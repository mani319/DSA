"""
An array contains both positive and negative numbers in random order.
Rearrange the array elements so that
    positive and negative numbers are placed alternatively.

Input: [-1, 2, -3, 4, 5, 6, -7, 8, 9]
Rearranged: [4, -3, 5, -1, 6, -7, 2, 8, 9]

Input: [12, 11, -13, -5, 6, -7, 5, -3, -6]
Rearranged: [12, -5, 5, -3, 11, -13, 6, -6, -7]

More Complex Methods:
1. Using 2 extra arrays for +ve and -ve numbers --> O(n), O(n)
"""


def segregate(arr):
    n = len(arr)

    j = 0
    for i in range(n):
        if(arr[i] < 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return j


def rearrangePosNegsAlternately(arr):
    n = len(arr)
    index = segregate(arr)

    pos = index
    neg = 0
    while(pos < n and neg < pos and arr[neg] < 0):
        arr[pos], arr[neg] = arr[neg], arr[pos]
        neg += 2
        pos += 1

    return arr


if __name__ == "__main__":
    arrays = [[-1, 2, -3, 4, 5, 6, -7, 8, 9],
              [12, 11, -13, -5, 6, -7, 5, -3, -6]]

    for array in arrays:
        print(array)
        print("Rearranged:", rearrangePosNegsAlternately(array))
        print("----------------------------------------------------")
