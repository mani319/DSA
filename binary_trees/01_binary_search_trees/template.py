class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(node, data):

    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node


if __name__ == "__main__":
    array = [4, 2, 5, 3, 6, 8, 1, 7]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])
