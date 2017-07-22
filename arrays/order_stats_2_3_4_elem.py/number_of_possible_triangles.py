

def numOfTriangles(arr):
    n = len(arr)
    arr.sort()
    count = 0

    for i in range(0, n-2):
        j = i + 1
        k = i + 2
        while(j < n):
            while(k < n and arr[i]+arr[j] > arr[k]):
                k += 1

            count += (k - j - 1)
            j += 1

    return count


if __name__ == "__main__":
    arrays = [[10, 21, 22, 100, 101, 200, 300],
              [4, 6, 3, 7]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(numOfTriangles(array))
