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


def inOrderPreSucUtil(root, key):
    if(root is None):
        return

    curr = root
    if(key == curr.data):

        if(curr.left):
            tmp = curr.left
            while(tmp.right):
                tmp = tmp.right

            inOrderPreSucUtil.pre = tmp

        if(curr.right):
            tmp = curr.right
            while(tmp.left):
                tmp = tmp.left

            inOrderPreSucUtil.suc = tmp

    elif(key < curr.data):
        inOrderPreSucUtil.suc = curr
        inOrderPreSucUtil(curr.left, key)

    else:
        inOrderPreSucUtil.pre = curr
        inOrderPreSucUtil(curr.right, key)

    return (inOrderPreSucUtil.pre, inOrderPreSucUtil.suc)


def inOrderPreSuc(root, key):
    inOrderPreSucUtil.pre = None
    inOrderPreSucUtil.suc = None

    inOrderPreSucUtil(root, key)
    if(inOrderPreSucUtil.pre):
        print("Inorder Predecessor is", inOrderPreSucUtil.pre.data)
    else:
        print("No Inorder Predecessor")

    if(inOrderPreSucUtil.suc):
        print("Inorder Successor is", inOrderPreSucUtil.suc.data)
    else:
        print("No Inorder Successor")


if __name__ == "__main__":
    array = [4, 2, 5, 3, 6, 8, 1, 7]

    root = None
    root = insert(root, array[0])
    for i in range(1, len(array)):
        insert(root, array[i])

    key = 1
    inOrderPreSuc(root, key)
