'''

Given a binary tree, find height of it. Height of empty tree is 0

Recursive:http://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
Iterative:http://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/

'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_height_recursive(a):
    if(a is None):
        return 0

    lHeight = find_height_recursive(a.left)
    rHeight = find_height_recursive(a.right)

    return max(lHeight+1, rHeight+1)


def find_height_iterative(a):
    if(a is None):
        return 0

    queue = []
    queue.append(a)
    height = 0

    while(True):
        count = len(queue)
        if(count == 0):
            return height

        height += 1

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

    print("1. Recursive height: ", find_height_recursive(root1))
    print("1. Iterative height: ", find_height_iterative(root1))

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.left.left.left = Node(6)

    print("2. Recursive height: ", find_height_recursive(root2))
    print("2. Iterative height: ", find_height_iterative(root2))
