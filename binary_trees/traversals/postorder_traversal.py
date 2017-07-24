class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrderRecursive(root):
    if(root is None):
        return

    postOrderRecursive(root.left)
    postOrderRecursive(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    postOrderRecursive(root)
