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


def numberOfTimes(head, val):
    count = 0

    curr = head
    while(curr):
        if(curr.data == val):
            count += 1
        curr = curr.next

    return count


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
    array = [1, 2, 3, 2, 1, 3, 1, 2, 1, 3]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("List: ", head)
    val = 3
    print("Number of times present:", numberOfTimes(head, val))
