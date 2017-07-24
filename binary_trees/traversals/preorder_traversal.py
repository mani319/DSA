class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderRecursive(root):
    if(root is None):
        return

    print(root.data, end=" ")
    preOrderRecursive(root.left)
    preOrderRecursive(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    preOrderRecursive(root)
