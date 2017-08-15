"""
"""


class Node:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.child = None


def flatten_multi_level_list(head):
    if(head is None):
        return

    curr = head
    last = head
    while(last.next):
        last = last.next

    while(curr):
        if(curr.child):
            last.next = curr.child
            while(last.next):
                last = last.next

        curr = curr.next

    return head
