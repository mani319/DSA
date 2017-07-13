

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def convert_to_mirror_tree(root):
    if(root is None):
        return None

    leftConvert = convert_to_mirror_tree(root.left)
    rightConvert = convert_to_mirror_tree(root.right)

    root.left, root.right = root.right, root.left


def print_inorder(root):
    if(root is None):
        return

    print_inorder(root.left)
    print(root.data, end=" ")
    print_inorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    convert_to_mirror_tree(root)
    print_inorder(root)
