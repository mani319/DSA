"""

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


def binarySearch(arr, low, high, key):
    if(low <= high):
        mid = low + (high-low)//2

        if(arr[mid] == key):
            return mid
        elif(key < arr[mid]):
            return binarySearch(arr, low, mid-1, key)
        else:
            return binarySearch(arr, mid+1, high, key)

    return -1


def searchElement(arr, key):
    n = len(arr)

    pivot = maxElementIndex(arr, 0, n-1)

    if(pivot != n-1):
        if(arr[pivot] == key):
            return pivot
        elif(key > arr[0]):
            return binarySearch(arr, 0, pivot-1, key)
        else:
            return binarySearch(arr, pivot+1, n-1, key)
    else:
        return binarySearch(arr, 0, n-1, key)

if __name__ == "__main__":
    arrays = [[5, 6, 7, 8, 9, 10, 1, 2, 3],
              [30, 40, 50, 10, 20],
              [3, 4, 5, 6, 1, 2],
              [1, 2, 3, 4, 5],
              [5, 6, 1, 2, 3, 4]]

    keys = [9, 50, 5, 4, 6]

    for i in range(len(arrays)):
        print(arrays[i], "-->", end=" ")
        print(searchElement(arrays[i], keys[i]))
