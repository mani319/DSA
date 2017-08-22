"""
You are given an unsorted array with both positive and negative elements.
Find the smallest positive number missing.
Time Complexity of O(n) using constant extra space.
You can modify the original array.

Examples

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2

More Complex Methods:
1. Naive method --> O(n^2), O(1)
2. Sorting --> O(nlogn), O(1)
3. Hashing --> O(n), O(n)
Below is the best solution
"""


def segregate(arr):
    n = len(arr)

    j = 0
    for i in range(n):
        if(arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return j


def array_modify(arr):
    n = len(arr)

    for i in range(n):
        if(abs(arr[i])-1 < n):
            if(arr[abs(arr[i])-1] > 0):
                arr[abs(arr[i])-1] *= -1

    for i in range(n):
        if(arr[i] > 0):
            return i+1

    return n+1


def firstPositiveMissing(arr):
    negs = segregate(arr)

    num = array_modify(arr[negs:])
    print("First positive number missing is:", num)


if __name__ == "__main__":
    arrays = [[0, 10, 2, -10, -20],
              [2, 3, 7, 6, 8, -1, -10, 15],
              [2, 3, -7, 6, 8, 1, -10, 15],
              [1, 1, 0, -1, -2]]

    for array in arrays:
        print(array)
        firstPositiveMissing(array)
        print("-----------------------------------------------------------")
