import math


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximum(root):
    if(root is None):
        return -math.inf

    lMax = maximum(root.left)
    rMax = maximum(root.right)

    return max(root.data, lMax, rMax)


def minimum(root):
    if(root is None):
        return math.inf

    lMin = minimum(root.left)
    rMin = minimum(root.right)

    return min(root.data, lMin, rMin)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(maximum(root))
    print(minimum(root))
