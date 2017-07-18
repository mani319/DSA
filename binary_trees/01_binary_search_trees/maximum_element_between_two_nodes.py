"""
Find the maximum element in the path from A to B in BST.
"""
import math


class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node


def maxElemInPath(lca, key):
    maxi = -math.inf

    curr = lca
    while(curr):
        if(key > curr.data):
            curr = curr.right

        elif(key < curr.data):
            maxi = max(curr.data, maxi)
            curr = curr.left

        else:
            maxi = max(key, maxi)
            break

    return maxi


def maximumElement(root, a, b):
    if(root is None):
        return

    lca = root
    while(lca):
        if(a > lca.data and b > lca.data):
            lca = lca.right

        elif(a < lca.data and b < lca.data):
            lca = lca.left

        else:
            break

    return max(maxElemInPath(lca, a), maxElemInPath(lca, b))


if __name__ == "__main__":
    array = [18, 36, 9, 6, 12, 10, 1, 8]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    print(maximumElement(root, 1, 10))
