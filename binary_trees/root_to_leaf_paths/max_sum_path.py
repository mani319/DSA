import math


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def maxSumPathUtil(root, paths, path_len):
    """
    Almost O(n^2) time and O(n) space
    """
    if(root is None):
        return

    paths[path_len] = root.data
    path_len += 1

    if(root.left is None and root.right is None):
        if(sum(paths[:path_len]) > maxSumPathUtil.maxSum):
            maxSumPathUtil.maxSum = sum(paths[:path_len])
            maxSumPathUtil.maxSumPath = paths[:path_len]
    else:
        maxSumPathUtil(root.left, paths, path_len)
        maxSumPathUtil(root.right, paths, path_len)


def maxSumPath(root):
    paths = [0]*10
    path_len = 0
    maxSumPathUtil.maxSum = -math.inf
    maxSumPathUtil.maxSumPath = []
    maxSumPathUtil(root, paths, path_len)
    print(maxSumPathUtil.maxSumPath)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(-4)

    maxSumPath(root)
