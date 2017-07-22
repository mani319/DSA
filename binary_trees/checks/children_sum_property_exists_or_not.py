"""
        10
       /  \
      8    2
     / \    \
    3   5    2
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    return(root.left is None and root.right is None)


def childrenSum(root):
    left_data = 0
    right_data = 0

    if(root is None or isLeaf(root)):
        return True

    if(root.left):
        left_data = root.left.data
    if(root.right):
        right_data = root.right.data

    return(root.data == left_data + right_data and
           childrenSum(root.left) and
           childrenSum(root.right))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(childrenSum(root))

    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(2)

    print(childrenSum(root))
