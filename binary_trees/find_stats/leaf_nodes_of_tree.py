

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_leaf_nodes(root):
    if(root is None):
        return 0

    if(root.left is None and root.right is None):
        print(root.data, end=" ")
        return 1

    leftLeaves = find_leaf_nodes(root.left)
    rightLeaves = find_leaf_nodes(root.right)

    return leftLeaves + rightLeaves


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print("\nNumber of leaf nodes:", find_leaf_nodes(root))
