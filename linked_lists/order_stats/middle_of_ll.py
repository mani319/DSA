"""
Given a singly linked list, find middle of the linked list.
For example, if given linked list is 1->2->3->4->5 then output should be 3.

If there are even nodes, then there would be two middle nodes,
    we need to print first middle element.
For example, if given linked list is 1->2->3->4->5->6 then output should be 3.
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


def getMiddle(head):
    if(head is None):
        return

    slowp, fastp = head, head.next
    while(fastp and fastp.next):
        slowp = slowp.next
        fastp = fastp.next.next

    return slowp


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
    array = [1, 2, 3, 4, 5, 6, 7]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print(getMiddle(head).data)
