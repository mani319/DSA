"""
"""


class Node:

    def __init__(self, val):
        self.data = val
        self.down = None
        self.next = None


def flatten_depth_wise(head):
    if(head is None):
        return

    last = head
    next = head.next

    if(head.down):
        head.next = flatten_depth_wise(head.down)

    if(next):
        last.next = flatten_depth_wise(next)

    return head
