"""
          26
        /   \
      10     3
    /    \     \
   4      6     3
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    return(root.left is None and root.right is None)


def sumTree(root):
    left_sum = 0
    right_sum = 0

    if(root is None or isLeaf(root)):
        return True

    if(root.left):
        if(isLeaf(root.left)):
            left_sum = root.left.data
        else:
            left_sum = 2 * root.left.data

    if(root.right):
        if(isLeaf(root.right)):
            right_sum = root.right.data
        else:
            right_sum = 2 * root.right.data

    return (root.data == left_sum + right_sum and
            sumTree(root.left) and sumTree(root.right))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(sumTree(root))

    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    print(sumTree(root))
