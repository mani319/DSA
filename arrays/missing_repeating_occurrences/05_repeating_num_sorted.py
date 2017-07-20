"""
Given a sorted array of n elements containing elements in range from 1 to n-1
i.e. one element occurs twice.
Find the number in O(log n) time & constant space.
"""


def searchRepeating(arr, low, high):
    if(low < high):
        mid = low + (high - low)//2

        if((mid > 0 and arr[mid] == arr[mid-1]) or
           (mid < high and arr[mid] == arr[mid+1])):
            return mid

        if(arr[mid] == mid+1):
            return searchRepeating(arr, mid+1, high)
        else:
            return searchRepeating(arr, low, mid-1)

    return -1


def elementRepeating(arr):
    n = len(arr)

    res = searchRepeating(arr, 0, n-1)
    if(res == -1):
        print("Not found")
    else:
        print("Repeating Element is:", arr[res])


if __name__ == "__main__":
    arrays = [[1, 2, 3, 4, 4],
              [1, 1, 2, 3, 4],
              [1, 2, 3, 3, 4, 5]]

    for array in arrays:
        print(array)
        elementRepeating(array)
        print("-----------------------------------------------------------")
