"""
You are given an array of 0s and 1s in random order.
Segregate 0s on left side and 1s on right side of the array.
Traverse array only once.

Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

Methods:http://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
"""


def segregate1(arr):
    '''
    Traverses twice - NOT EFFICIENT
    '''
    n = len(arr)

    count = 0
    for i in range(n):
        if(arr[i] == 0):
            count += 1

    for i in range(n):
        if(i < count):
            arr[i] = 0
        else:
            arr[i] = 1


def segregate2(arr):
    '''
    Traverses only once - EFFICIENT
    '''
    n = len(arr)

    l, r = 0, n-1
    while(l < r):
        while(l < r and arr[l] == 0):
            l += 1

        while(l < r and arr[r] == 1):
            r -= 1

        if(l < r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    array = [0, 1, 0, 1, 0, 0, 1, 1, 1]
    segregate2(array)
    print(array)
