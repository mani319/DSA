class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def isLeaf(root):
    return(root.left is None and root.right is None)


def sameLevelUtil(root, level):
    if(root is None):
        return True

    if(isLeaf(root)):
        if(check.leaf_level == 0):
            check.leaf_level = level
            return True

        return (check.leaf_level == level)

    return (sameLevelUtil(root.left, level+1) and
            sameLevelUtil(root.right, level+1))


def check(root):
    level = 0
    check.leaf_level = 0    # Can also use leaf_level = [0] and pass it
    print(sameLevelUtil(root, level))


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    check(root1)

    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(9)
    root.left.left.left = Node(1)
    root.left.right.left = Node(2)

    check(root)
