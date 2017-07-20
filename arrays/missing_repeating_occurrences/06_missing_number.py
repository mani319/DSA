"""
You are given a list of n-1 integers.
These integers are in the range of 1 to n.
There are no duplicates in list. One of the integers is missing in the list.
Find the number in O(n) time & constant space.
"""


def xor_method(arr):
    n = len(arr)

    xor = 0
    for i in range(n):
        xor ^= arr[i]

    for i in range(1, n+2):
        xor ^= i

    print("Num missing:", xor)


def sum_method(arr):
    n = len(arr)

    arth_sum = (n+1)*(n+2)//2
    actual_sum = 0
    for i in range(n):
        actual_sum += arr[i]

    missing = arth_sum - actual_sum
    print("Num missing:", missing)


def elementMissing(arr):
    xor_method(arr)
    sum_method(arr)


if __name__ == "__main__":
    arrays = [[1, 2, 4, 6, 3, 7, 8],
              [1, 2, 4, 5, 6]]

    for array in arrays:
        print(array)
        elementMissing(array)
        print("-----------------------------------------------------------")
