class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def ancestors(root, val):
    if(root is None):
        return False

    if(root.data == val):
        return True

    if(ancestors(root.left, val) or ancestors(root.right, val)):
        print(root.data, end=" ")
        return True

    return False


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    val = 5
    ancestors(root, val)
