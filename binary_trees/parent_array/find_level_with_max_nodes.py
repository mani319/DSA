"""
Print Level Order of Binary Tree represented by Parent array
A given array represents a tree in such a way that
    the array value gives the parent node of that particular index.
The value of the root node index would always be -1.
Find the height of the tree.

Input: parent[] = {1 5 5 2 2 -1 3}
Output: 2
The given array represents following Binary Tree
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6
"""


def findDepth(arr, i, depth):
    if(depth[i] != -1):
        return

    if(arr[i] == -1):
        depth[i] = 0
        return

    if(depth[arr[i]] == -1):
        findDepth(arr, arr[i], depth)

    depth[i] = depth[arr[i]] + 1


def depthWiseMaxNodes(arr, n):
    depth = [-1 for i in range(n)]

    for i in range(n):
        findDepth(arr, i, depth)

    hash_map = {}
    for i in range(n):
        try:
            hash_map[depth[i]].append(i)
        except KeyError:
            hash_map[depth[i]] = [i]

    maxi = -1
    ans = -1
    for key, value in hash_map.items():
        if((maxi == len(value) and ans < key) or maxi < len(value)):
            ans = key
            maxi = len(value)

    print (ans)


if __name__ == "__main__":
    arrays = [[-1, 0, 0, 1, 1, 3, 5],
              [4, 3, -1, -1, 1, 2, 7, 3, 1, 4, 2, 1, 2],
              [5, -1, 1, 1, 5, 2]]

    for arr in arrays:
        n = len(arr)
        depthWiseMaxNodes(arr, n)
