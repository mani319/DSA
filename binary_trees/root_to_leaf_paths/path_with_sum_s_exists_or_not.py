class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def isLeaf(root):
    return (root.left is None and root.right is None)


def path_with_sum_exists(root, sum):
    if(root is None):
        return False

    rem_sum = sum - root.data
    if(rem_sum == 0 and isLeaf(root)):
        return True

    if(path_with_sum_exists(root.left, rem_sum)):
        return True

    if(path_with_sum_exists(root.right, rem_sum)):
        return True

    return False


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    sums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for sum in sums:
        print("sum:", sum, end=" ")
        if(path_with_sum_exists(root, sum)):
            print("Exists!")
        else:
            print("Doesn't Exists!")
