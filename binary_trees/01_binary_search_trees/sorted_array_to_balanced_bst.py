"""
Given a sorted array.
Write a function that creates a Balanced BST using array elements.

Following is a simple algorithm:
1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.

Time Complexity: O(n)
  T(n) = 2T(n/2) + C
  T(n) -->  Time taken for an array of size n
   C   -->  Constant (Finding middle of array and linking root to left
                      and right subtrees take constant time)
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertUtil(arr, low, high):
    if(low <= high):
        mid = low + (high-low)//2

        root = Node(arr[mid])
        root.left = convertUtil(arr, low, mid-1)
        root.right = convertUtil(arr, mid+1, high)

        return root

    return None


def printInOrder(root):
    if(root is None):
        return

    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


def convertToBalancedTree(arr):
    n = len(arr)

    low = 0
    high = n-1
    root = convertUtil(arr, low, high)
    printInOrder(root)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    convertToBalancedTree(array)
