'''

Top View of Tree

'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def top_view_recursive_util(a, m, hd, level):
    if(a is None):
        return

    top_view_recursive_util(a.left, m, hd-1, level+1)

    if hd in m:
        if(level < m[hd][1]):
            m.update({hd: [a.data, level]})
    else:
        m[hd] = [a.data, level]

    top_view_recursive_util(a.right, m, hd+1, level+1)


def top_view_recursive(a):
    m = {}
    hd = 0
    level = 0
    top_view_recursive_util(a, m, hd, level)

    for key, value in m.items():
        print (value[0], end=" ")


def top_view_iterative(a):
    if(a is None):
        return

    queue = []
    m = {}
    hd = 0
    queue.append([a, hd])

    while(len(queue) > 0):
        data = queue.pop(0)
        node = data[0]
        hd = data[1]

        if(hd not in m):
            m[hd] = node.data

        if(node.left is not None):
            queue.append([node.left, hd-1])
        if(node.right is not None):
            queue.append([node.right, hd+1])

    for key, value in m.items():
        print (value, end=" ")


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    top_view_recursive(root1)
    print()
    top_view_iterative(root1)
    print()

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.right.right = Node(9)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.left.left.left = Node(6)
    root2.left.right.right = Node(7)
    root2.left.right.right.right = Node(8)

    top_view_recursive(root2)
    print()
    top_view_iterative(root2)
    print()
