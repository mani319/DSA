class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def mirrors_or_not(a, b):
    if(a is None and b is None):
        return True

    if(a is None or b is None):
        return False

    return (a.data == b.data and
            mirrors_or_not(a.left, b.right) and
            mirrors_or_not(a.right, b.left))


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    print("1. Check: ", mirrors_or_not(root1, root2))

    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.left = Node(5)
    root2.right.right = Node(4)

    print("2. Check: ", mirrors_or_not(root1, root2))
