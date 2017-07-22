class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST1(root, left=None, right=None):
    if(root is None):
        return True

    if(left and root.data <= left.data):
        return False

    if(right and root.data >= right.data):
        return False

    return(isBST1(root.left, left, root) and
           isBST1(root.right, root, right))


def isBST2_Util(root):
    if(root is None):
        return True

    if(not isBST2_Util(root.left)):
        return False

    if(isBST2_Util.prev and root.data <= isBST2_Util.prev.data):
        return False

    isBST2_Util.prev = root

    return isBST2_Util(root.right)


def isBST2(root):
    isBST2_Util.prev = None
    return isBST2_Util(root)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(isBST1(root))
    print(isBST2(root))
    print("----------------------------------")

    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(4)

    print(isBST1(root))
    print(isBST2(root))
