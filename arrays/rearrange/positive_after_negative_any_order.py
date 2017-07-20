"""
Given an array of positive and negative numbers,
arrange them such that all -ve integers appear before all the +ve integers
 **** ORDER DOEN'T MATTER ****

Input: [-1, 2, -3, 4, 5, 6, -7, 8, 9]
Rearranged: [-1, -3, -7, 4, 5, 6, 2, 8, 9]

Input: [12, 11, -13, -5, 6, -7, 5, -3, -6]
Rearranged: [-13, -5, -7, -3, -6, 12, 5, 11, 6]

More Complex Methods:
1. Using a copy array and then arranging original --> O(n), O(n)
"""


def segregate(arr):
    n = len(arr)

    j = 0
    for i in range(n):
        if(arr[i] < 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


if __name__ == "__main__":
    arrays = [[-1, 2, -3, 4, 5, 6, -7, 8, 9],
              [12, 11, -13, -5, 6, -7, 5, -3, -6]]

    for array in arrays:
        print(array)
        print("Rearranged:", segregate(array))
        print("----------------------------------------------------")
