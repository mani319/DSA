'''

Two trees are identical when they have same data and arrangement of data is
also same. To identify if two trees are identical, we need to traverse both
trees simultaneously, and while traversing we need to compare data and
children of the trees.

Recursive:http://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
Iterative:http://www.geeksforgeeks.org/iterative-function-check-two-trees-identical/

'''


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def identical_or_not_recursive(a, b):
    if(a is None and b is None):
        return True

    if(a is None or b is None):
        return False

    return (a.data == b.data and
            identical_or_not_recursive(a.left, b.left) and
            identical_or_not_recursive(a.right, b.right))


def identical_or_not_iterative(a, b):
    if(a is None and b is None):
        return True

    if(a is None or b is None):
        return False

    queue1 = []
    queue2 = []
    queue1.append(a)
    queue2.append(b)

    while(len(queue1) > 0 and len(queue2) > 0):
        n1 = queue1.pop(0)
        n2 = queue2.pop(0)

        if(n1.data != n2.data):
            return False

        if(n1.left is not None and n2.left is not None):
            queue1.append(n1.left)
            queue2.append(n2.left)
        elif(n1.left is not None or n2.left is not None):
            return False

        if(n1.right is not None and n2.right is not None):
            queue1.append(n1.right)
            queue2.append(n2.right)
        elif(n1.right is not None or n2.right is not None):
            return False

    return True


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

    print("1. Recursive check: ", identical_or_not_recursive(root1, root2))
    print("1. Iterative check: ", identical_or_not_iterative(root1, root2))

    root3 = Node(1)
    root3.left = Node(2)
    root3.right = Node(3)
    root3.left.left = Node(4)
    root3.left.right = Node(6)

    print("2. Recursive check: ", identical_or_not_recursive(root1, root3))
    print("2. Iterative check: ", identical_or_not_iterative(root1, root3))

    root4 = Node(1)
    root4.left = Node(2)
    root4.right = Node(3)
    root4.left.left = Node(4)

    print("3. Recursive check: ", identical_or_not_recursive(root1, root4))
    print("3. Iterative check: ", identical_or_not_iterative(root1, root4))
