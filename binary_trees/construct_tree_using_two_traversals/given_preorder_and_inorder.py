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


def construct_util(preOrder, inOrder, inStart, inEnd):
    if(inStart > inEnd):
        return None

    tNode = Node(preOrder[construct_util.preIndex])
    construct_util.preIndex += 1

    if(inStart == inEnd):
        return tNode

    inIndex = find_index(inOrder, inStart, inEnd, tNode.data)

    tNode.left = construct_util(preOrder, inOrder, inStart, inIndex-1)
    tNode.right = construct_util(preOrder, inOrder, inIndex+1, inEnd)

    return tNode


def construct(preOrder, inOrder):
    n = len(inOrder)
    # static variable to traverse preOrder array
    construct_util.preIndex = 0
    inStart = 0
    inEnd = n-1
    root = construct_util(preOrder, inOrder, inStart, inEnd)
    print_inorder(root)


def print_inorder(root):
    if(root is None):
        return

    print_inorder(root.left)
    print(root.data, end=" ")
    print_inorder(root.right)


if __name__ == "__main__":
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    construct(preOrder, inOrder)
