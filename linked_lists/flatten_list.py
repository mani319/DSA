"""
Given a linked list where every node represents a linked list and
    contains two pointers of its type:
    (i) Pointer to next node in the main list (right)
    (ii) Pointer to a linked list where this node is head (down)
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45

Write a function flatten() to flatten the lists into a single linked list.
The flattened linked list should also be sorted.
For example, for the above input list,
    output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.
"""


class Node:

    def __init__(self, value):
        self.data = value
        self.right = None
        self.down = None


def insert_at_end(head, value):
    curr = head
    while(curr.down):
        curr = curr.down

    curr.down = Node(value)


def merge(headA, headB):
    res = None

    if(headA is None):
        return headB

    if(headB is None):
        return headA

    if(headA.data < headB.data):
        res = headA
        res.down = merge(headA.down, headB)
    else:
        res = headB
        res.down = merge(headA, headB.down)

    return res


def flatten(head):
    if(head is None or head.right is None):
        return head

    head.right = flatten(head.right)    # Imp step

    return merge(head, head.right)


def print_list(message, head):
    if (head is None):
        return

    print(message, end="")
    temp = head
    while(temp):
        print (temp.data, "->", end=" ")
        temp = temp.down
    print("None")


if __name__ == "__main__":
    head = Node(5)
    insert_at_end(head, 7)
    insert_at_end(head, 8)
    insert_at_end(head, 30)

    head.right = Node(10)
    insert_at_end(head.right, 20)

    head.right.right = Node(19)
    insert_at_end(head.right.right, 22)
    insert_at_end(head.right.right, 50)

    head.right.right.right = Node(28)
    insert_at_end(head.right.right.right, 35)
    insert_at_end(head.right.right.right, 40)
    insert_at_end(head.right.right.right, 45)

    head = flatten(head)
    print_list("Flatten List: ", head)
