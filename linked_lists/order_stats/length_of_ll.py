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


def lengthIterative(head):
    count = 0

    curr = head
    while(curr):
        count += 1
        curr = curr.next

    return count


def lengthRecursive(head):
    if(head is None):
        return 0

    return(1 + lengthRecursive(head.next))


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
    array = [1, 2, 3, 4, 5, 6, 7, 9, 10, 8]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("List: ", head)
    print("Length of List:", lengthIterative(head))
    print("Length of List:", lengthRecursive(head))
