'''



'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_max_width_iterative(a):
    if(a is None):
        return 0

    queue = []
    max_width = 0
    queue.append(a)

    while(True):
        count = len(queue)
        if(count == 0):
            return max_width

        max_width = max(max_width, count)

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

    print("1. Iterative max width: ", find_max_width_iterative(root1))

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.left.right = Node(7)

    print("2. Iterative max width: ", find_max_width_iterative(root2))

    root3 = Node(1)

    print("3. Iterative max width: ", find_max_width_iterative(root3))
