"""
Given an almost sorted array where only two elements are swapped,
how to sort the array efficiently?

Examples:-

Input:  arr[] = {10, 20, 60, 40, 50, 30}
// 30 and 60 are swapped
Output: arr[] = {10, 20, 30, 40, 50, 60}

Input:  arr[] = {10, 20, 40, 30, 50, 60}
// 30 and 40 are swapped
Output: arr[] = {10, 20, 30, 40, 50, 60}

Input:   arr[] = {1, 5, 3}
// 3 and 5 are swapped
Output:  arr[] = {1, 3, 5}
"""


def twoElemSwapped1(arr):
    n = len(arr)

    first, last = None, None
    for i in range(0, n-1):
        if(arr[i] > arr[i+1]):
            if(first is None):
                first = i
                last = i+1
            else:
                last = i+1

    arr[first], arr[last] = arr[last], arr[first]


def twoElemSwapped2(arr):
    n = len(arr)

    for i in range(0, n-1):
        if(arr[i] > arr[i+1]):
            j = i + 1
            while(j < n and arr[i] > arr[j]):
                j += 1

            arr[i], arr[j-1] = arr[j-1], arr[i]
            break


if __name__ == "__main__":
    arrays = [[10, 20, 60, 40, 50, 30],
              [10, 20, 40, 30, 50, 60],
              [1, 5, 3]]

    for array in arrays:
        print(array, "-->", end=" ")
        twoElemSwapped2(array)
        print(array)
