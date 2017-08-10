"""

"""


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def searchIterative(head, val):
    curr = head
    while(curr):
        if(curr.data == val):
            return True
        curr = curr.next

    return False


def searchRecursive(head, val):
    if(head is None):
        return False

    if(head.data == val):
        return True

    return searchRecursive(head.next, val)


def print_list(message, head):
    if (head is None):
        return

    print(message, end="")
    temp = head
    while(temp):
        print (temp.data, "->", end=" ")
        temp = temp.next
    print("None")


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 9, 10, 8]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("List: ", head)
    vals = [1, 11, 7, 12, 9]
    for val in vals:
        print("Present or not:", searchIterative(head, val))
        print("Present or not:", searchRecursive(head, val))
        print("---------------------------")
