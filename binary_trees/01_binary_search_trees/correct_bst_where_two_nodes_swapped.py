class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def correctUtil(root):
    if(root is None):
        return

    correctUtil(root.left)      # Left Recursion

    if(correctUtil.prev and correctUtil.prev.data > root.data):
        if(correctUtil.first is None):
            correctUtil.first = correctUtil.prev
            correctUtil.last = root
        else:
            correctUtil.last = root

    correctUtil.prev = root

    correctUtil(root.right)     # Right Recursion


def correctBST(root):
    correctUtil.first, correctUtil.last = None, None
    correctUtil.prev = None
    correctUtil(root)

    correctUtil.first.data, correctUtil.last.data = correctUtil.last.data, correctUtil.first.data


def printInorder(root):
    if(root is None):
        return

    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


if __name__ == "__main__":
    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(12)

    printInorder(root)
    print()
    correctBST(root)
    printInorder(root)
    print()
