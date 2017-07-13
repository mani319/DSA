'''
'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_index(arr, start, end, data):
    for i in range(start, end+1):
        if(arr[i] is data):
            return i


def construct_util(postOrder, inOrder, inStart, inEnd):
    if(inStart > inEnd):
        return None

    tNode = Node(postOrder[construct_util.postIndex])
    construct_util.postIndex -= 1

    if(inStart == inEnd):
        return tNode

    inIndex = find_index(inOrder, inStart, inEnd, tNode.data)

    tNode.right = construct_util(postOrder, inOrder, inIndex+1, inEnd)
    tNode.left = construct_util(postOrder, inOrder, inStart, inIndex-1)

    return tNode


def construct(postOrder, inOrder):
    n = len(inOrder)
    # static variable to traverse postOrder array
    construct_util.postIndex = n-1
    inStart = 0
    inEnd = n-1
    root = construct_util(postOrder, inOrder, inStart, inEnd)
    print_preorder(root)


def print_preorder(root):
    if(root is None):
        return

    print(root.data, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


if __name__ == "__main__":
    postOrder = [8, 4, 5, 2, 6, 7, 3, 1]
    inOrder = [4, 8, 2, 5, 1, 6, 3, 7]
    construct(postOrder, inOrder)
