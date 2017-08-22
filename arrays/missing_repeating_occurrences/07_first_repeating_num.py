"""
Given an array of integers, find the first repeating element in it.
We need to find the element that occurs more than once and
    whose index of first occurrence is smallest.

Examples:

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]

A Simple Solution is to use two nested loops.
The outer loop picks an element one by one,
    the inner loop checks whether the element is repeated or not.
Once we find an element that repeats, we break the loops and print the element.
Time Complexity of this solution is O(n^2)

We can Use Sorting to solve the problem in O(nLogn) time.
Following are detailed steps.
1) Copy the given array to an auxiliary array temp[].
2) Sort the temp array using a O(nLogn) time sorting algorithm.
3) Scan the input array from left to right. For every element,
    count its occurrences in temp[] using binary search.
As soon as we find an element that occurs more than once, we return the element
Time Complexity of this solution is O(nLogn) time. Space: O(n)

Below is the best method
"""


def hashing_method(arr):
    n = len(arr)

    mini = -1
    hash_map = {}
    for i in range(n-1, -1, -1):    # Traverse from right to left
        if(arr[i] in hash_map):
            mini = i
        else:
            hash_map[arr[i]] = True

    if(mini == -1):
        print("No repeating elements")
    else:
        print("First Repeating Element:", arr[mini])


def firstRepeating(arr):
    hashing_method(arr)


if __name__ == "__main__":
    arrays = [[10, 5, 3, 4, 3, 5, 6],
              [6, 10, 5, 4, 9, 120, 4, 6, 10],
              [1, 2, 3, 4]]

    for array in arrays:
        print(array)
        firstRepeating(array)
        print("-----------------------------------------------------------")
