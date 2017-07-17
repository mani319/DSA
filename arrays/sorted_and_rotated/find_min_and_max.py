"""
Find pivot in sorted and rotated array
Array should be of form first increasing till pivot and then decreasing
Eg:
[5, 6, 7, 8, 9, 10, 1, 2, 3]
[30, 40, 50, 10, 20]
"""


def maxElementIndex(arr, low, high):
    if(low <= high):
        mid = low + (high-low)//2

        if(mid < high and arr[mid] > arr[mid+1]):
            return mid
        if(mid > low and arr[mid] < arr[mid-1]):
            return mid-1
        if(arr[mid] > arr[mid-1]):
            return maxElementIndex(arr, mid+1, high)
        else:
            return maxElementIndex(arr, low, mid-1)

    return high


def minElementIndex(arr, low, high):
    if(low <= high):
        mid = low + (high-low)//2

        if(mid < high and arr[mid] > arr[mid+1]):
            return mid+1
        if(mid > low and arr[mid] < arr[mid-1]):
            return mid
        if(arr[mid] > arr[mid-1]):
            return minElementIndex(arr, mid+1, high)
        else:
            return minElementIndex(arr, low, mid-1)

    return 0


if __name__ == "__main__":
    arrays = [[5, 6, 7, 8, 9, 10, 1, 2, 3],
              [30, 40, 50, 10, 20],
              [3, 4, 5, 6, 1, 2],
              [1, 2, 3, 4, 5],
              [5, 6, 1, 2, 3, 4]]

    for array in arrays:
        n = len(array)
        print(array, "-->", end=" ")
        print("max index:", maxElementIndex(array, 0, n-1), ",", end=" ")
        print("min index:", minElementIndex(array, 0, n-1))
