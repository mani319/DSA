"""
You are given a DLL with one pointer of each node pointing to
    the next node just like in a single link list.
The second pointer however CAN point to any node in the list and
    not just the previous node.

Now write a program in O(n) time to duplicate this list.
That is, write a program which will create a copy of this list.

Method1:http://www.geeksforgeeks.org/clone-linked-list-next-arbit-pointer-set-2/
Method2(Best):http://www.geeksforgeeks.org/clone-linked-list-next-random-pointer-o1-space/
"""


class Node():
    def __init__(self, data):
        self.data = data
        self.arbit = None
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def clone_list1(head):
    '''
    Hashing Method:
    Not best - O(n) time, O(n) extra space
    '''
    


def clone_list2(head):
    '''
    Best Method - O(n) time, O(1) extra space
    '''
    curr = head
    while(curr):
        n_next = curr.next
        curr.next = Node(curr.data)
        curr.next.next = n_next
        curr = n_next

    curr = head
    while(curr):
        curr.next.arbit = curr.arbit.next
        curr = curr.next.next

    original, copy = head, head.next
    res = copy
    while(original and copy):
        original.next = original.next.next

        if(copy.next):
            copy.next = copy.next.next

        original = original.next
        copy = copy.next

    return res


def print_list(msg, head):
    print(msg)

    print("Data\tNext\tArbit")
    while(head):
        if(head.next):
            print(head.data, '\t', head.next.data, '\t', head.arbit.data)
        else:
            print(head.data, '\t', None, '\t', head.arbit.data)
        head = head.next

    print()


if __name__ == "__main__":
    head = Node(1)
    insert_at_end(head, 2)
    insert_at_end(head, 3)
    insert_at_end(head, 4)
    insert_at_end(head, 5)

    head.arbit = head.next.next
    head.next.arbit = head
    head.next.next.arbit = head.next.next.next.next
    head.next.next.next.arbit = head.next.next.next.next
    head.next.next.next.next.arbit = head.next

    print_list("Original List: ", head)
    res = clone_list2(head)
    print_list("Cloned List: ", res)
