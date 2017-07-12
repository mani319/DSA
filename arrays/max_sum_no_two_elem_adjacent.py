'''

Given an array of positive numbers.
Find the maximum sum of a subsequence with the constraint
    that no 2 numbers in the sequence should be adjacent in the array.

Approach:http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
Loop for all elements in arr[] and maintain two sums incl and excl where
incl = Max sum including the previous element and
excl = Max sum excluding the previous element

Max sum excluding the current element will be max(incl, excl) and
max sum including the current element will be excl + current element
(Note that only excl is considered because elements cannot be adjacent).

At the end of the loop return max of incl and excl.

'''


def max_sum_no_two_elements_adjacent(arr):
    n = len(arr)
    excl = 0
    incl = 0

    for i in range(n):
        new_excl = max(incl, excl)
        incl = excl + arr[i]
        excl = new_excl

    return max(incl, excl)


if __name__ == "__main__":
    arrays = [[5, 5, 10, 100, 10, 5],
              [1, 2, 3],
              [1, 20, 3],
              [5,  5, 10, 40, 50, 35],
              [3, 2, 7, 10],
              [3, 2, 5, 10, 7]]

    for array in arrays:
        print(array, "Max sum:", max_sum_no_two_elements_adjacent(array))
