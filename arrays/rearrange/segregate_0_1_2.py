"""
Given an array A[] consisting 0s, 1s and 2s,
write a function that sorts A[].
The functions should put all 0s first, then all 1s and all 2s in last.

Example:-
Input = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
Output = {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

INEFFICIENT METHOD:(2 Traversals)
Counting number of 0s, 1s and 2s in array and then inserting those many

EFFICIENT METHOD:(1 Traversal)
The array is divided into four sections:
a[0..Lo-1] zeroes
a[Lo..Mid-] ones
a[Mid..Hi] unknown
a[Hi+1..N-1] twos

Method:http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
"""


def segregate(arr):
    n = len(arr)

    low, mid, high = 0, 0, n-1
    while(mid <= high):
        if(arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif(arr[mid] == 1):
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


if __name__ == "__main__":
    array = [0, 2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 2, 1, 0, 1]
    segregate(array)
    print(array)
