class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelUtil(root, k, level):
    if(root is None):
        return None

    if(level == k+1):
        print(root.data, end=" ")

    levelUtil(root.left, k, level+1)
    levelUtil(root.right, k, level+1)


def nodesAtKDistance(root, k):
    level = 1
    levelUtil(root, k, level)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    k = 2
    nodesAtKDistance(root, k)
