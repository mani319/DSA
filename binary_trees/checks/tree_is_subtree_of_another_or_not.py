"""
Check whether tree2 is subtree of tree1 or not
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areIdentical(root1, root2):
    if(root1 is None and root2 is None):
        return True

    if(root1 is None or root2 is None):
        return False

    return (root1.data == root2.data and
            areIdentical(root1.left, root2.left) and
            areIdentical(root1.right, root2.right))


def isSubTree1(root1, root2):
    '''
    O(n^2) time, O(n) stack memory
    '''
    if(root2 is None):
        return True

    if(root1 is None):
        return False

    if(areIdentical(root1, root2)):
        return True

    return (isSubTree1(root1.left, root2) or
            isSubTree1(root1.right, root2))


def storeInOrder(root, inOrder):
    if(root is None):
        return inOrder

    storeInOrder(root.left, inOrder)
    inOrder.append(root.data)
    storeInOrder(root.right, inOrder)

    return inOrder


def storePreOrder(root, preOrder):
    if(root is None):
        return preOrder

    preOrder.append(root.data)
    storePreOrder(root.left, preOrder)
    storePreOrder(root.right, preOrder)

    return preOrder


def isSubList(list1, list2):
    n = len(list1)
    m = len(list2)

    i = 0
    while(i < n and list1[i] != list2[0]):
        i += 1

    if(i == n):
        return False

    j = 0
    while(j < m and i < n and list1[i] == list2[j]):
        i += 1
        j += 1

    return (j == m)


def isSubTree2(root1, root2):
    """
    O(n) time and O(n) space
    """
    if(root2 is None):
        return True

    if(root1 is None):
        return False

    inOrder1 = storeInOrder(root1, [])
    inOrder2 = storeInOrder(root2, [])
    if(not isSubList(inOrder1, inOrder2)):
        return False

    preOrder1 = storePreOrder(root1, [])
    preOrder2 = storePreOrder(root2, [])
    if(not isSubList(preOrder1, preOrder2)):
        return False

    return True


if __name__ == "__main__":
    root1 = Node(26)
    root1.right = Node(3)
    root1.right.right = Node(3)
    root1.left = Node(10)
    root1.left.left = Node(4)
    root1.left.left.right = Node(30)
    root1.left.right = Node(6)

    root2 = Node(10)
    root2.right = Node(6)
    root2.left = Node(4)
    root2.left.right = Node(30)

    print(isSubTree1(root1, root2))
    print(isSubTree2(root1, root2))
