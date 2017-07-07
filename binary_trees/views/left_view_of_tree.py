'''

Left View of Tree

'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def left_view_recursive_util(a, level, max_level):
    if(a is None):
        return

    if(max_level[0] < level):
        print(a.data, end=" ")
        max_level[0] = level

    left_view_recursive_util(a.left, level+1, max_level)
    left_view_recursive_util(a.right, level+1, max_level)


def left_view_recursive(a):
    max_level = [0]
    level = 1
    left_view_recursive_util(a, level, max_level)


def left_view_iterative(a):
    if(a is None):
        return

    queue = []
    queue.append(a)

    while(True):
        count = len(queue)
        if(count == 0):
            break

        print(queue[0].data, end=" ")

        while(count > 0):
            node = queue.pop(0)

            if(node.left is not None):
                queue.append(node.left)
            if(node.right is not None):
                queue.append(node.right)

            count -= 1


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    left_view_recursive(root1)
    print()
    left_view_iterative(root1)
    print()

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.left.left.left = Node(6)
    root2.left.right.right = Node(7)
    root2.left.right.right.right = Node(8)

    left_view_recursive(root2)
    print()
    left_view_iterative(root2)
    print()
