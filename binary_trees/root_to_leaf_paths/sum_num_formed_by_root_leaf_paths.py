class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    return(root.left is None and root.right is None)


def sumUtil(root, val):
    if(root is None):
        return 0

    val = (val*10) + root.data
    if(isLeaf(root)):
        return val

    return(sumUtil(root.left, val) + sumUtil(root.right, val))


def sum_numbers_formed_by_root_leaf_paths(root):
    val = 0
    return sumUtil(root, val)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print(sum_numbers_formed_by_root_leaf_paths(root))
