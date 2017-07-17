

def rainWaterTrapped(arr):
    n = len(arr)
    waterTrapped = 0

    lMax = [0]*n
    lMax[0] = arr[0]
    for i in range(1, n):
        lMax[i] = max(lMax[i-1], arr[i])

    rMax = [0]*n
    rMax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rMax[i] = max(rMax[i+1], arr[i])

    for i in range(n):
        waterTrapped += min(lMax[i], rMax[i]) - arr[i]

    return waterTrapped


if __name__ == "__main__":
    arrays = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
              [2, 0, 2],
              [3, 0, 0, 2, 0, 4]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(rainWaterTrapped(array))
