class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def nodesInRange(root, low, high):
    if(root is None):
        return 0

    if(low <= root.data and high >= root.data):
        return (1 +
                nodesInRange(root.left, low, high) +
                nodesInRange(root.right, low, high))

    elif(low < root.data):
        return nodesInRange(root.left, low, high)

    else:
        return nodesInRange(root.right, low, high)


def insert(node, data):

    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node


if __name__ == "__main__":
    array = [10, 5, 50, 1, 40, 100]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    low = 5
    high = 45
    print(nodesInRange(root, low, high))

    low = 1
    high = 50
    print(nodesInRange(root, low, high))
