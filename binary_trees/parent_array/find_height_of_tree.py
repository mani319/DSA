"""
Find Height of Binary Tree represented by Parent array
A given array represents a tree in such a way that
    the array value gives the parent node of that particular index.
The value of the root node index would always be -1.
Find the height of the tree.

Input: parent[] = {1 5 5 2 2 -1 3}
Output: 4
The given array represents following Binary Tree
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6
"""


def calcDepth(arr, i, depth):
    if(depth[i] != 0):
        return

    if(arr[i] == -1):
        depth[i] = 1
        return

    if(depth[arr[i]] == 0):
        calcDepth(arr, arr[i], depth)

    depth[i] = depth[arr[i]] + 1


def findHeight(arr, n):
    depth = [0 for i in range(n)]

    for i in range(n):
        calcDepth(arr, i, depth)

    return max(depth)


if __name__ == "__main__":
    arrays = [[-1, 0, 0, 1, 1, 3, 5],
              [1, 5, 5, 2, 2, -1, 3]]

    for arr in arrays:
        n = len(arr)
        print ("Height:", findHeight(arr, n))
