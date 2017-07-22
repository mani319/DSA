class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isHeightBalanced(root, height):
    if(root is None):
        return True

    lh, rh = [0], [0]

    leftBalanced = isHeightBalanced(root.left, lh)
    rightBalanced = isHeightBalanced(root.right, rh)

    height[0] = max(lh[0], rh[0]) + 1

    return (abs(lh[0]-rh[0]) <= 1 and leftBalanced and rightBalanced)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(isHeightBalanced(root, [0]))

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print(isHeightBalanced(root, [0]))
