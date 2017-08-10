"""
Given a Linked List of integers,
write a function to modify the linked list such that all even numbers appear
    before all the odd numbers in the modified linked list.
Also, keep the order of even and odd numbers same.

Examples:

Input: 17->15->8->12->10->5->4->1->7->6->NULL
Output: 8->12->10->4->6->17->15->5->1->7->NULL

Input: 8->12->10->5->4->1->6->NULL
Output: 8->12->10->4->6->5->1->NULL

Method:http://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

One Inefficient Method is:
1. Go to the last node of list with one pointer
2. Now start a new pointer from head and move all odd valued nodes to end
Why not efficient??
    - won't preserve the order
    - Traverses list twice

Below is the method which preserves order and traverses only once
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


def segregateEvenOdd(head):

    evenFirst, evenLast = None, None
    oddFirst, oddLast = None, None
    curr = head
    while(curr):
        if(curr.data & 1):      # Odd
            if(oddFirst):
                oddLast.next = curr
                oddLast = oddLast.next
            else:
                oddFirst = curr
                oddLast = oddFirst

        else:
            if(evenFirst):
                evenLast.next = curr
                evenLast = evenLast.next
            else:
                evenFirst = curr
                evenLast = evenFirst

        curr = curr.next

    if(evenFirst and oddFirst):
        evenLast.next = oddFirst
        oddLast.next = None
        head = evenFirst

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
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("List: ", head)
    head = segregateEvenOdd(head)
    print_list("Segregated List: ", head)
