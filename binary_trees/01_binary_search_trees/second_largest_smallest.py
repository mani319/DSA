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


def secondSmallestUtil(root):
    if(root is None):
        return

    secondSmallestUtil(root.left)

    secondSmallestUtil.count += 1
    if(secondSmallestUtil.count == 2):
        print(root.data)

    secondSmallestUtil(root.right)


def secondSmallest(root):
    secondSmallestUtil.count = 0

    secondSmallestUtil(root)


def secondLargestUtil(root):
    if(root is None):
        return

    secondLargestUtil(root.right)

    secondLargestUtil.count += 1
    if(secondLargestUtil.count == 2):
        print(root.data)

    secondLargestUtil(root.left)


def secondLargest(root):
    secondLargestUtil.count = 0

    secondLargestUtil(root)


if __name__ == "__main__":
    array = [4, 2, 5, 3, 6, 8, 1, 7]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    secondSmallest(root)
    secondLargest(root)
