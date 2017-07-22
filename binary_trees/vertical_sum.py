class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def vertical_sum_util(root, m, hd):
    if(root is None):
        return

    vertical_sum_util(root.left, m, hd-1)

    if(hd in m.keys()):
        m[hd] += root.data
    else:
        m[hd] = root.data

    vertical_sum_util(root.right, m, hd+1)


def vertical_sum(root):
    m = {}
    hd = 0
    vertical_sum_util(root, m, hd)

    for key, value in m.items():
        print(value, end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    vertical_sum(root)
