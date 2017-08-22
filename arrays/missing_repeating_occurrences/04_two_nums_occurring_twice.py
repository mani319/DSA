"""
You are given an array of n+2 elements.
All elements of the array are in range 1 to n.
And all elements occur once except two numbers which occur twice.
Find the two repeating numbers in O(n) time & constant space.

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

    for i in range(1, n-1):
        xor ^= i

    set_bit = xor & ~(xor-1)

    x, y = 0, 0
    for i in range(n):
        if(arr[i] & set_bit):
            x ^= arr[i]
        else:
            y ^= arr[i]

    for i in range(1, n-1):
        if(i & set_bit):
            x ^= i
        else:
            y ^= i

    print("Nums occuring twice:", x, y)


def array_modify(arr):
    n = len(arr)

    print("Nums occuring twice:", end=" ")
    for i in range(n):
        if(arr[abs(arr[i])-1] > 0):
            arr[abs(arr[i])-1] *= -1
        else:
            print(abs(arr[i]), end=" ")
    print()


def elementsThatAppearsTwice(arr):
    xor_method(arr)
    # sum_product_method(arr)
    array_modify(arr)


if __name__ == "__main__":
    arrays = [[4, 2, 4, 5, 2, 3, 1],
              [1, 3, 2, 2, 1]]

    for array in arrays:
        print(array)
        elementsThatAppearsTwice(array)
        print("-----------------------------------------------------------")
