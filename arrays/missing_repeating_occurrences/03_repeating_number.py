"""
You are given an array of n+1 elements.
All elements of the array are in range 1 to n.
And all elements occur once except one number which occurs twice.
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

    for i in range(1, n):
        xor ^= i

    print("Num occuring twice:", xor)


def sum_method(arr):
    n = len(arr)

    arth_sum = (n-1)*(n)//2
    actual_sum = 0
    for i in range(n):
        actual_sum += arr[i]

    repeating = actual_sum - arth_sum
    print("Num occuring twice:", repeating)


def array_modify(arr):
    n = len(arr)

    for i in range(n):
        if(arr[abs(arr[i])-1] >= 0):
            arr[abs(arr[i])-1] *= -1
        else:
            print("Num occuring twice:", abs(arr[i]))
            break


def elementThatAppearsTwice(arr):
    xor_method(arr)
    sum_method(arr)
    array_modify(arr)


if __name__ == "__main__":
    arrays = [[7, 3, 5, 4, 5, 6, 2, 1],
              [2, 3, 5, 4, 6, 1, 4]]

    for array in arrays:
        print(array)
        elementThatAppearsTwice(array)
        print("-----------------------------------------------------------")
