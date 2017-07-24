class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def subTreesInRange(root, low, high):
    if(root is None):
        return True

    leftInRange = subTreesInRange(root.left, low, high)
    rightInRange = subTreesInRange(root.right, low, high)
    rootInRange = (low <= root.data and high >= root.data)

    if(leftInRange and rightInRange and rootInRange):
        subTreesInRange.count += 1
        return True

    return False


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

    low = 1
    high = 45
    subTreesInRange.count = 0
    subTreesInRange(root, low, high)
    print(subTreesInRange.count)
