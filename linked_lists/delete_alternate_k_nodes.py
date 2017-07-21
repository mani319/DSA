class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def delete_alternate_k_nodes(head, k):
    curr = head
    prev = None
    while(curr):
        count = 0
        while(curr and count < k):
            prev = curr
            curr = curr.next
            count += 1

        if(curr is None):
            return head

        count = 0
        while(curr and count < k):
            prev.next = curr.next
            del curr
            curr = prev.next
            count += 1

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
    insert_at_end(headA, 2)
    insert_at_end(headA, 3)
    insert_at_end(headA, 4)
    insert_at_end(headA, 5)
    insert_at_end(headA, 6)
    insert_at_end(headA, 7)
    insert_at_end(headA, 8)
    insert_at_end(headA, 9)
    insert_at_end(headA, 10)
    insert_at_end(headA, 11)

    k = 3

    print_list("ListA: ", headA)
    print_list("Swapped ListA: ", delete_alternate_k_nodes(headA, k))
    print()

    headB = Node(1)
    insert_at_end(headB, 2)
    insert_at_end(headB, 3)
    insert_at_end(headB, 4)
    insert_at_end(headB, 5)
    insert_at_end(headB, 6)
    insert_at_end(headB, 7)
    insert_at_end(headB, 8)
    insert_at_end(headB, 9)

    k = 3

    print_list("ListB: ", headB)
    print_list("Swapped ListB: ", delete_alternate_k_nodes(headB, k))
    print()

    headC = Node(1)
    insert_at_end(headC, 2)

    k = 3

    print_list("ListC: ", headC)
    print_list("Swapped ListC: ", delete_alternate_k_nodes(headC, k))
    print()
