def maxElementIndex(arr, low, high):
    while(low <= high):
        mid = low + (high-low)//2

        if(mid < high and arr[mid] > arr[mid+1]):
            return mid
        if(mid > low and arr[mid] < arr[mid-1]):
            return mid-1
        if(arr[mid] > arr[mid-1]):
            low = mid+1
        else:
            high = mid-1

    return high


def sumPairExists(arr, sum):
    n = len(arr)

    pivot = maxElementIndex(arr, 0, n-1)

    l = (pivot + 1) % n
    r = pivot
    while(l != r):
        if(arr[l] + arr[r] == sum):
            return True
        elif(arr[l] + arr[r] < sum):
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n

    return False


if __name__ == "__main__":
    array = [5, 6, 7, 8, 9, 10, 1, 2, 3]

    sums = [1, 2, 4, 10, 30, 11, 17, 14, 20]

    for i in range(len(sums)):
        print(array, "sum:", sums[i], "-->", end=" ")
        print(sumPairExists(array, sums[i]))
