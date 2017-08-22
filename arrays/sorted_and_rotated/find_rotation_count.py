def minElementIndex(arr, low, high):
    while(low <= high):
        mid = low + (high-low)//2

        if(mid < high and arr[mid] > arr[mid+1]):
            return mid+1
        if(mid > low and arr[mid] < arr[mid-1]):
            return mid
        if(arr[mid] > arr[mid-1]):
            low = mid+1
        else:
            high = mid-1

    return 0


def rotationCount(arr):
    n = len(arr)
    return minElementIndex(arr, 0, n-1)


if __name__ == "__main__":
    arrays = [[5, 6, 7, 8, 9, 10, 1, 2, 3],
              [30, 40, 50, 10, 20],
              [4, 5, 6, 1, 2, 3],
              [1, 2, 3, 4, 5],
              [5, 6, 1, 2, 3, 4]]

    for array in arrays:
        n = len(array)
        print(array, "-->", end=" ")
        print("elements rotated:", rotationCount(array))
