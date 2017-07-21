class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def merge_lists_recursive(headA, headB):
    newList = None

    if(headA is None):
        return headB

    if(headB is None):
        return headA

    if(headA.data < headB.data):
        newList = headA
        newList.next = merge_lists_recursive(headA.next, headB)
    else:
        newList = headB
        newList.next = merge_lists_recursive(headA, headB.next)

    return newList


def merge_lists_iterative(headA, headB):
    newList = Node(0)
    newHead = newList

    while(headA or headB):
        if(headA is None):
            newList.next = headB
            break

        if(headB is None):
            newList.next = headA
            break

        if(headA.data < headB.data):
            newList.next = headA
            headA = headA.next
        else:
            newList.next = headB
            headB = headB.next
        newList = newList.next

    return newHead.next


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

    print_list("List1: ", headA)

    headB = Node(2)
    insert_at_end(headB, 4)
    insert_at_end(headB, 6)
    insert_at_end(headB, 8)

    print_list("List2: ", headB)

    print_list("Iter Merged List: ", merge_lists_iterative(headA, headB))
    # print_list("Recr Merged List: ", merge_lists_recursive(headA, headB))
