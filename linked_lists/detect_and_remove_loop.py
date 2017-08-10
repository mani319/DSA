"""

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


def detect_and_remove_loop(head):
    if(head is None):
        return None

    slowp, fastp = head, head
    while(fastp and fastp.next):
        slowp = slowp.next
        fastp = fastp.next.next
        if(slowp == fastp):
            break

    if(slowp == fastp):
        print("Loop Exists and removing....")

        slowp = head
        while(slowp.next != fastp.next):
            slowp = slowp.next
            fastp = fastp.next

        fastp.next = None

    else:
        print("No loop in list")
        return None

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
    array = [1, 2, 3, 4, 5]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    head.next.next.next.next.next = head.next.next

    head = detect_and_remove_loop(head)
    print_list("List after deleting loop: ", head)
