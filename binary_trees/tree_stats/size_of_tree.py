

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_size(root):
    if(root is None):
        return 0

    leftSize = find_size(root.left)
    rightSize = find_size(root.right)

    return leftSize + rightSize + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print(find_size(root))
