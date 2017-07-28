"""
Given an array that stores a complete Binary Search Tree,
write a function that efficiently prints the given array in ascending order.
For example,
given an array [4, 2, 5, 1, 3], the function should print 1, 2, 3, 4, 5
        4
       / \
      2   5
     / \
    1   3

Method:
Inorder traversal of BST prints it in ascending order.
The only trick is to modify recursion termination condition in
    standard Inorder Tree Traversal.
"""


def printSortedOrder(arr, start, size):
    if(start <= size):
        printSortedOrder(arr, 2*start+1, size)
        print(arr[start], end=" ")
        printSortedOrder(arr, 2*start+2, size)

    return


if __name__ == "__main__":
    arrays = [[4, 2, 5, 1, 3]]

    for array in arrays:
        n = len(array)
        start = 0
        printSortedOrder(array, start, n-1)
        print()
