# Python program for implementation of Quicksort Sort


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = low               # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1

    arr[i], arr[high] = arr[high], arr[i]
    return i


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
# Function to do Quick sort
def quickSort_recursive(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort_recursive(arr, low, pi-1)
        quickSort_recursive(arr, pi+1, high)


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSort_iterative(arr, l, h):

    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# A utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print (arr[i], end=" ")
    print()


if __name__ == "__main__":
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort_recursive(arr, 0, n-1)
    print ("Sorted array is:", end=" ")
    printArray(arr, len(arr))

    arr1 = [10, 7, 8, 9, 1, 5]
    n = len(arr1)
    quickSort_iterative(arr1, 0, n-1)
    print ("Sorted array is:", end=" ")
    printArray(arr1, len(arr1))
