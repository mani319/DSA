class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.pre = None
        self.suc = None


def pip_Util(root):
    if(root is None):
        return

    pip_Util(root.left)     # Left

    root.pre = pip_Util.prev
    pip_Util.prev = root

    pip_Util(root.right)    # Right


def populate_inorder_predecessors(root):
    pip_Util.prev = None
    pip_Util(root)


def pis_Util(root):
    if(root is None):
        return

    pis_Util(root.right)    # Right

    root.suc = pis_Util.next
    pis_Util.next = root

    pis_Util(root.left)     # Left


def populate_inorder_successors(root):
    pis_Util.next = None
    pis_Util(root)


def print_All(root):
    if(root is None):
        return

    print_All(root.left)

    if(root.suc and root.pre):
        print(root.data, root.pre.data, root.suc.data)
    elif(root.suc):
        print(root.data, -1, root.suc.data)
    elif(root.pre):
        print(root.data, root.pre.data, -1)

    print_All(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    populate_inorder_predecessors(root)
    populate_inorder_successors(root)
    print_All(root)
