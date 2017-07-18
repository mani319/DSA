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


def lcaRecursive(root, a, b):
    if(root is None):
        return

    if(a > root.data and b > root.data):
        return lcaRecursive(root.right, a, b)

    if(a < root.data and b < root.data):
        return lcaRecursive(root.left, a, b)

    return root


def lcaIterative(root, a, b):
    if(root is None):
        return

    while(root):

        if(a > root.data and b > root.data):
            root = root.right

        elif(a < root.data and b < root.data):
            root = root.left

        else:
            break

    return root


if __name__ == "__main__":
    array = [4, 2, 5, 3, 6, 8, 1, 7]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    print(lcaRecursive(root, 1, 3).data)
    print(lcaIterative(root, 1, 3).data)

    print()

    print(lcaRecursive(root, 1, 5).data)
    print(lcaIterative(root, 1, 5).data)
