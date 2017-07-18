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


def smallestValueRecursive(root):
    if(root is None):
        return

    curr = root
    if(curr.left):
        return smallestValueRecursive(curr.left)

    return curr.data


def smallestValueIterative(root):
    if(root is None):
        return

    curr = root
    while(curr.left):
        curr = curr.left

    return curr.data


def largestValueRecursive(root):
    if(root is None):
        return

    curr = root
    if(curr.right):
        return largestValueRecursive(curr.right)

    return curr.data


def largestValueIterative(root):
    if(root is None):
        return

    curr = root
    while(curr.right):
        curr = curr.right

    return curr.data


if __name__ == "__main__":
    array = [4, 2, 5, 3, 6, 8, 1, 7]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    print("Recursive Smallest Value:", smallestValueRecursive(root))
    print("Iterative Smallest Value:", smallestValueIterative(root))

    print("Recursive Largest Value:", largestValueRecursive(root))
    print("Iterative Largest Value:", largestValueIterative(root))
