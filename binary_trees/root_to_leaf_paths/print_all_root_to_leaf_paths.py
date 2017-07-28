class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def root_to_leaf_paths_util(root, paths, path_len):
    if(root is None):
        return

    paths[path_len] = root.data
    path_len += 1

    if(root.left is None and root.right is None):
        print(paths[:path_len])
    else:
        root_to_leaf_paths_util(root.left, paths, path_len)
        root_to_leaf_paths_util(root.right, paths, path_len)


def root_to_leaf_paths(root):
    paths = [0]*1000
    path_len = 0
    root_to_leaf_paths_util(root, paths, path_len)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    root_to_leaf_paths(root)
