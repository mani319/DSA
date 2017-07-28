class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelUtil(root, val, level):
    if(root is None):
        return -1

    if(root.data == val):
        return level

    return max(levelUtil(root.left, val, level+1),
               levelUtil(root.right, val, level+1))


def getLevel(root, val):
    level = 1
    return levelUtil(root, val, level)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    val = 3
    print(getLevel(root, val))
