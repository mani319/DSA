"""
Given an array of positive and negative numbers,
arrange them such that all -ve integers appear before all the +ve integers
 **** SAME ORDER SHOULD BE MAINTAINED ****

Input: [-1, 2, -3, 4, 5, 6, -7, 8, 9]
Rearranged: [-1, -3, -7, 2, 4, 5, 6, 8, 9]

Input: [12, 11, -13, -5, 6, -7, 5, -3, -6]
Rearranged: [-13, -5, -7, -3, -6, 12, 11, 6, 5]

More Complex Methods:
1. Using a copy array and then arranging original --> O(n), O(n)
2. Modified Insertion sort --> O(n^2), O(1)

Below is the best method : Modified Merge Sort
Steps:
1. Reverse Lp and Rn. We get [Lp] -> [Lp'] and [Rn] -> [Rn']
[Ln Lp Rn Rp] -> [Ln Lp’ Rn’ Rp]

2. Reverse [Lp’ Rn’]. We get [Rn Lp].
[Ln Lp’ Rn’ Rp] -> [Ln Rn Lp Rp]
"""


def reverse(arr, l, r):
    while(l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


def modified_merge(arr, low, mid, high):
    i = low
    while(i <= mid and arr[i] < 0):
        i += 1

    j = mid+1
    while(j <= high and arr[j] < 0):
        j += 1

    reverse(arr, i, mid)
    reverse(arr, mid+1, j-1)
    reverse(arr, i, j-1)


def modified_merge_sort(arr, low, high):
    if(low < high):
        mid = low + (high - low)//2

        modified_merge_sort(arr, low, mid)
        modified_merge_sort(arr, mid+1, high)

        modified_merge(arr, low, mid, high)


def segregate(arr):
    n = len(arr)

    modified_merge_sort(arr, 0, n-1)

    return arr


if __name__ == "__main__":
    arrays = [[-1, 2, -3, 4, 5, 6, -7, 8, 9],
              [12, 11, -13, -5, 6, -7, 5, -3, -6]]

    for array in arrays:
        print(array)
        print("Rearranged:", segregate(array))
        print("----------------------------------------------------")
