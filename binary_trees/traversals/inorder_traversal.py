

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrderRecursive(root):
    if(root is None):
        return

    inOrderRecursive(root.left)
    print(root.data, end=" ")
    inOrderRecursive(root.right)


def inOrderIterativeUsingStack(root):
    if(root is None):
        return

    st = []
    curr = root
    while(True):
        if(curr):
            st.append(curr)
            curr = curr.left

        elif(len(st) > 0):
            curr = st.pop()
            print(curr.data, end=" ")
            curr = curr.right

        else:
            break


def inOrderIterativeMorris(root):

    curr = root
    while(curr):
        if(curr.left is None):
            print (curr.data, end=" ")
            curr = curr.right
        else:
            tmp = curr.left
            while(tmp.right and tmp.right != curr):
                tmp = tmp.right

            if(tmp.right is None):
                tmp.right = curr
                curr = curr.left
            else:
                tmp.right = None
                print (curr.data, end=" ")
                curr = curr.right


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    inOrderRecursive(root)
    print()
    inOrderIterativeUsingStack(root)
    print()
    inOrderIterativeMorris(root)
