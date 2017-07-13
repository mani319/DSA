

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def convert_to_sum_tree(root):
    if(root is None):
        return 0

    original_data = root.data

    leftConvert = convert_to_sum_tree(root.left)
    rightConvert = convert_to_sum_tree(root.right)

    root.data = leftConvert + rightConvert

    return root.data + original_data


def print_inorder(root):
    if(root is None):
        return

    print_inorder(root.left)
    print(root.data, end=" ")
    print_inorder(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    convert_to_sum_tree(root)
    print_inorder(root)
