"""
Given two arrays which are duplicates of each other except one element,
that is one element from one of the array is missing.
(Need not be in same order of original array)
we need to find that missing element in O(n)

Examples:

Input:  arr1[] = {1, 4, 5, 7, 9}
        arr2[] = {4, 5, 7, 9}
Output: 1
1 is missing from second array.

Input: arr1[] = {2, 3, 4, 5}
       arr2[] = {2, 3, 4, 5, 6}
Output: 6
6 is missing from first array.

One simple solution is to iterate over arrays and check element by element
    and flag the missing element when an unmatch is found,
    but this solution requires linear time over size of array.
"""


def xor_method(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    xor = 0
    for i in range(n1):
        xor ^= arr1[i]

    for i in range(n2):
        xor ^= arr2[i]

    print("Missing Elem: ", xor)


def binary_search_util(arr1, arr2, n):
    if(n == 1 or arr1[0] != arr2[0]):
        print("Missing Elem: ", arr1[0])
        return

    low = 0
    high = n-1
    while(low < high):
        mid = low + (high - low)//2

        if(arr1[mid] == arr2[mid]):
            low = mid
        else:
            high = mid

        if(low == high-1):
            break

    print("Missing Elem: ", arr1[high])


def binary_search_method(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    if(n1 == n2 - 1):
        binary_search_util(arr2, arr1, n2)
    elif(n2 == n1 - 1):
        binary_search_util(arr1, arr2, n1)
    else:
        print("Invalid Input")


def elementMissing(arr1, arr2):
    xor_method(arr1, arr2)
    binary_search_method(arr1, arr2)


if __name__ == "__main__":
    array1 = [[2, 3, 4, 5],
              [1, 4, 5, 7, 9]]

    array2 = [[2, 3, 4, 5, 6],
              [4, 5, 7, 9]]

    for i in range(len(array1)):
        print(array1[i], array2[i])
        elementMissing(array1[i], array2[i])
        print("-----------------------------------------------------------")
