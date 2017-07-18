"""
Array should be sorted before passing
"""


def binarySearch(arr, low, high, key):
    if(low <= high):
        mid = low + (high-low)//2

        if(key == arr[mid]):
            return mid
        if(key < arr[mid]):
            return binarySearch(arr, low, mid-1, key)
        else:
            return binarySearch(arr, mid+1, high, key)

    return -1


if __name__ == "__main__":
    arrays = [[1, 2, 3, 5, 6, 7, 8, 9, 10],
              [1, 2, 3, 5, 6, 7, 8, 9, 10],
              [1, 2, 3, 5, 6, 7, 8, 9, 10],
              [1, 2, 3, 5, 6, 7, 8, 9, 10]]
    keys = [5, 10, 3, 100]

    for i in range(len(arrays)):
        n = len(arrays[i])
        print(arrays[i], "key:", keys[i], "-->", "index:", end=" ")
        print(binarySearch(arrays[i], 0, n-1, keys[i]))
