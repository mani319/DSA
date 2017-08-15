"""
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def identical_check_iterative(head1, head2):

    while(head1 and head2):
        if(head1.data != head2.data):
            return False

        head1 = head1.next
        head2 = head2.next

    return (not head1 and not head2)


def identical_check_recursive(head1, head2):
    if(head1 is None and head2 is None):
        return True

    if(head1 is None or head2 is None):
        return False

    return (head1.data == head2.data and
            identical_check_recursive(head1.next, head2.next))


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
    array1 = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(array1)

    head1 = Node(array1[0])
    for i in range(1, n):
        insert_at_end(head1, array1[i])

    array2 = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(array2)

    head2 = Node(array2[0])
    for i in range(1, n):
        insert_at_end(head2, array2[i])

    print (identical_check_iterative(head1, head2))
    print (identical_check_recursive(head1, head2))
