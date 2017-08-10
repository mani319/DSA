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


def delete_list(head):

    curr = head
    while(curr):
        n_next = curr.next
        del curr
        curr = n_next

    head = None     # Just this line is enough to delete list in Python
    return head


def print_list(message, head):
    if (head is None):
        print("List Empty")
        return

    print(message, end="")
    temp = head
    while(temp):
        print (temp.data, "->", end=" ")
        temp = temp.next
    print("None")


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("List: ", head)
    head = delete_list(head)
    print_list("List: ", head)
