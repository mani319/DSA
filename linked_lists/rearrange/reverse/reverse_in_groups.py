class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, value):
    curr = head
    while(curr.next):
        curr = curr.next

    curr.next = Node(value)


def reverse_in_groups(head, k):
    count = 0
    curr = head
    prev = None
    while(curr and count < k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    if(curr):
        head.next = reverse_in_groups(curr, k)

    return prev


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
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(array)

    head = Node(array[0])
    for i in range(1, n):
        insert_at_end(head, array[i])

    print_list("Original List: ", head)

    k = 3
    head = reverse_in_groups(head, k)
    print_list("Reversed List: ", head)
