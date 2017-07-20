"""
Given an unsorted array.
Array contains even number of occurrences for all numbers except two numbers.
Find the two numbers in O(n) time complexity and O(1) extra space

More Complex Methods:
1. Naive Method --> O(n^2), O(1)
2. Sort and search --> O(nlogn), O(1)
3. Hashing --> O(n), O(n)
"""


def xor_method(arr):
    n = len(arr)

    xor = 0
    for i in range(n):
        xor ^= arr[i]

    set_bit = xor & ~(xor-1)

    x, y = 0, 0
    for i in range(n):
        if(set_bit & arr[i]):
            x ^= arr[i]
        else:
            y ^= arr[i]

    print("Two Elements occuring odd times are:", x, y)


def twoNumbers(arr):
    xor_method(arr)


if __name__ == "__main__":
    arrays = [[12, 23, 34, 12, 12, 23, 12, 45],
              [4, 4, 100, 5000, 4, 4, 4, 4, 100, 100],
              [10, 20],
              [4, 2, 4, 5, 2, 3, 3, 1]]

    for array in arrays:
        print(array)
        twoNumbers(array)
        print("-----------------------------------------------------------")
