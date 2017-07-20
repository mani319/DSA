"""
Given an array of integers.
All numbers occur twice except one number which occurs once.
Find the number in O(n) time & constant space.

A Simple Solution is to run two nested loops.
The outer loop picks all elements one by one and
    inner loop counts number of occurrences of the element picked by outer loop
** Time complexity of this solution is O(n2).

A Better Solution is to use Hashing.
Use array elements as key and their counts as value.
Create an empty hash table.
One by one traverse the given array elements and store counts.
** Time complexity of this solution is O(n).
   But it requires extra space O(n) for hashing.

Below are the best possible Solutions
"""


def xor_method(arr):
    n = len(arr)

    xor = 0
    for i in range(n):
        xor ^= arr[i]

    print("Num occuring only once:", xor)


def elementThatAppearsOnce(arr):
    xor_method(arr)


if __name__ == "__main__":
    arrays = [[7, 3, 5, 4, 5, 3, 4],
              [2, 3, 5, 4, 5, 3, 4]]

    for array in arrays:
        print(array)
        elementThatAppearsOnce(array)
        print("-----------------------------------------------------------")
