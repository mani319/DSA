

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def find_diameter(root, height):
    if(root is None):
        return 0

    lh, rh = [0], [0]

    leftDiameter = find_diameter(root.left, lh)
    rightDiameter = find_diameter(root.right, rh)

    height[0] = max(lh[0], rh[0]) + 1

    return max(lh[0]+rh[0]+1, leftDiameter, rightDiameter)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print(find_diameter(root, [0]))
