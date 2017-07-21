class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def swap_alternate_nodes(head):
    if(head is None or head.next is None):
        return head

    curr = head
    prev = None
    while(curr and curr.next):
        n_next = curr.next
        curr.next = n_next.next
        n_next.next = curr
        if(curr is head):
            head = n_next
        else:
            prev.next = n_next
        prev = curr
        curr = curr.next

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
    headA = Node(1)
    insert_at_end(headA, 3)
    insert_at_end(headA, 5)
    insert_at_end(headA, 7)
    insert_at_end(headA, 9)
    insert_at_end(headA, 11)
    insert_at_end(headA, 13)

    print_list("ListA: ", headA)
    print_list("Swapped ListA: ", swap_alternate_nodes(headA))
    print()

    headB = Node(2)
    insert_at_end(headB, 4)
    insert_at_end(headB, 6)
    insert_at_end(headB, 8)

    print_list("ListB: ", headB)
    print_list("Swapped ListB: ", swap_alternate_nodes(headB))
    print()

    headC = Node(2)

    print_list("ListC: ", headC)
    print_list("Swapped ListC: ", swap_alternate_nodes(headC))
