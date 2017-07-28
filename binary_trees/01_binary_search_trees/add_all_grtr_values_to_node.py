class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def addUtil(root):
    if(root is None):
        return

    addUtil(root.right)

    addUtil.sum += root.data
    root.data = addUtil.sum

    addUtil(root.left)

    return root


def add_all_grtr_values(root):
    addUtil.sum = 0
    root = addUtil(root)
    printInOrder(root)


def printInOrder(root):
    if(root is None):
        return

    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


def insert(node, data):

    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node


if __name__ == "__main__":
    array = [8, 4, 12, 2, 6, 10, 14]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    add_all_grtr_values(root)
