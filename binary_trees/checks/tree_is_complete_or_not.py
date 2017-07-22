class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isCompleteTree_Iterative(root):
    """
    Using Level Order Traversal
    """
    if(root is None):
        return True

    queue = []
    queue.append(root)
    flag = False
    while(len(queue) > 0):
        root = queue.pop(0)

        if(root.left):
            if(flag):
                return False
            queue.append(root.left)
        else:
            flag = True

        if(root.right):
            if(flag):
                return False
            queue.append(root.right)
        else:
            flag = True

    return True


def size_of_tree(root):
    if(root is None):
        return 0

    return (size_of_tree(root.left) + 1 + size_of_tree(root.right))


def isCompleteTree_RecursiveUtil(root, index, nodes):
    if(root is None):
        return True

    if(index >= nodes):
        return False

    return (isCompleteTree_RecursiveUtil(root.left, 2*index+1, nodes) and
            isCompleteTree_RecursiveUtil(root.right, 2*index+2, nodes))


def isCompleteTree_Recursive(root):
    nodes = size_of_tree(root)
    index = 0
    return isCompleteTree_RecursiveUtil(root, index, nodes)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print(isCompleteTree_Iterative(root))
    print(isCompleteTree_Recursive(root))
    print("------------------")

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print(isCompleteTree_Iterative(root))
    print(isCompleteTree_Recursive(root))
