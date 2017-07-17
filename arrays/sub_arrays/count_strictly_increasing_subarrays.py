

def numOfSubarrays(arr):
    n = len(arr)
    count = 0
    start = 0
    for i in range(1, n):
        if(arr[i] > arr[i-1]):
            count += i - start
        else:
            start = i

    return count


if __name__ == "__main__":
    arrays = [[1, 2, 2, 4],
              [1, 4, 3],
              [1, 2, 3, 4],
              [1, 2, 3, 4, 5],
              [3, 5, 4, 4, 6, 7, 8, 11, 3]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(numOfSubarrays(array))
