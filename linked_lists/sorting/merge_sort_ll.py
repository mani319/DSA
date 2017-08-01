"""
Merge sort is often preferred for sorting a linked list.
The slow random-access performance of a linked list makes some other algorithms
    (such as quicksort) perform poorly,
    and others (such as heapsort) completely impossible.
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
    slowp, fastp = head, head.next
    while(fastp and fastp.next):
        slowp = slowp.next
        fastp = fastp.next.next

    return slowp


def merge(headA, headB):
    res = None

    if(headA is None):
        return headB

    if(headB is None):
        return headA

    if(headA.data < headB.data):
        res = headA
        res.next = merge(headA.next, headB)
    else:
        res = headB
        res.next = merge(headA, headB.next)

    return res


def mergeSort(head):
    if(head is None or head.next is None):
        return head

    middle = getMiddle(head)
    nextOfMiddle = middle.next
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(nextOfMiddle)

    final = merge(left, right)

    return final


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
    array = [3, 8, 5, 4, 1, 9, 6, 2, 7]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("Original List: ", head)
    head = mergeSort(head)
    print_list("Sorted List: ", head)
