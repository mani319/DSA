

def rainWaterTrapped1(arr):
    '''
    O(n) time and O(n) space
    '''
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


def rainWaterTrapped2(arr):
    '''
    O(n) time, O(1) space
    '''
    n = len(arr)
    waterTrapped = 0

    lMax, rMax = 0, 0
    l, r = 0, n-1
    while(l <= r):
        if(arr[l] < arr[r]):
            if(arr[l] > lMax):
                lMax = arr[l]
            else:
                waterTrapped += lMax - arr[l]
                l += 1
        else:
            if(arr[r] > rMax):
                rMax = arr[r]
            else:
                waterTrapped += rMax - arr[r]
                r -= 1

    return waterTrapped


if __name__ == "__main__":
    arrays = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
              [2, 0, 2],
              [3, 0, 0, 2, 0, 4]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(rainWaterTrapped1(array))
        print(array, "-->", end=" ")
        print(rainWaterTrapped2(array))
        print("----------------------------------------------")
