import math


def findLeaders(arr):
    """
    Scan from right side of array
    """
    n = len(arr)
    leaders = []

    maxi = -math.inf
    for i in range(n-1, -1, -1):
        if(arr[i] > maxi):
            maxi = arr[i]
            leaders.append(maxi)

    return leaders


if __name__ == "__main__":
    array = [18, 17, 4, 3, 5, 2]
    print(findLeaders(array))
