'''



'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_min_depth_recursive(a):
    if(a is None):
        return 0

    if(a.left is None and a.right is None):
        return 1

    if(a.right is None):
        return find_min_depth_recursive(a.left)+1

    if(a.left is None):
        return find_min_depth_recursive(a.right)+1

    return min(find_min_depth_recursive(a.left)+1,
               find_min_depth_recursive(a.right)+1)


def find_min_depth_iterative(a):
    if(a is None):
        return 0

    queue = []
    depth = 0
    queue.append(a)

    while(True):
        count = len(queue)
        depth += 1

        while(count > 0):
            node = queue.pop(0)

            if(node.left is None and node.right is None):
                return depth

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

    print("1. Recursive min depth: ", find_min_depth_recursive(root1))
    print("1. Iterative min depth: ", find_min_depth_iterative(root1))

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.left.right = Node(7)

    print("2. Recursive min depth: ", find_min_depth_recursive(root2))
    print("2. Iterative min depth: ", find_min_depth_iterative(root2))

    root3 = Node(1)

    print("3. Recursive min depth: ", find_min_depth_recursive(root3))
    print("3. Iterative min depth: ", find_min_depth_iterative(root3))
