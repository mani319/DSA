"""
Number is represented in linked list
    such that each digit corresponds to a node in linked list. Add 1 to it.

Eg:-
1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to it
    should change it to (2->0->0->0)
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


def addUtil(head):
    if(head is None):
        return 1

    val = head.data + addUtil(head.next)

    head.data = val % 10
    carry = val // 10

    return carry


def addOnetoList(head):
    carry = addUtil(head)

    if(carry):
        newNode = Node(carry)
        newNode.next = head
        head = newNode

    return head


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
    array = [9, 9, 9, 9]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("Original List: ", head)
    head = addOnetoList(head)
    print_list("List after adding 1: ", head)
