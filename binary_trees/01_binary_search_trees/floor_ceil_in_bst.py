class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def fcUtil(root, val):
    if(root is None):
        return

    if(val == root.data):
        fcUtil.floor = root.data
        fcUtil.ceil = root.data
    elif(val < root.data):
        fcUtil.ceil = root.data
        fcUtil(root.left, val)
    else:
        fcUtil.floor = root.data
        fcUtil(root.right, val)


def floor_ceil(root):
    fcUtil.floor = -1
    fcUtil.ceil = -1
    val = 9
    fcUtil(root, val)
    print(val, fcUtil.floor, fcUtil.ceil)


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

    floor_ceil(root)
