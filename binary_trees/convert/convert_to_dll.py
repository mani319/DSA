class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertUtil1(root, head):
    """
    Reverse Inorder Traversal
    """
    if(root is None):
        return

    convertUtil1(root.right, head)   # Right

    # Insert at beginning of DLL
    root.right = head[0]
    if(head[0]):
        head[0].left = root
    head[0] = root

    convertUtil1(root.left, head)   # Left


def convert_to_dll1(root):
    head = [None]
    convertUtil1(root, head)

    node = head[0]
    while(node):
        print(node.data, end=" ")
        node = node.right


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    convert_to_dll1(root)
