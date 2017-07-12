# Recursive Python program for insertion sort
# Recursive function to sort an array using insertion sort


def insertionSort_recursive(arr, n):
    # base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertionSort_recursive(arr, n-1)

    # Insert last element at its correct position in sorted array.
    last = arr[n-1]
    j = n-2

    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = last


def insertionSort_iterative(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


# A utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print (arr[i], end=" ")
    print()


if __name__ == "__main__":
    # Driver program to test insertion sort
    arr = [12, 11, 13, 5, 6, 15, 18, 3, 2]
    n = len(arr)
    insertionSort_recursive(arr, n)
    print("Sorted Array is:", end=" ")
    printArray(arr, n)

    arr1 = [12, 11, 13, 5, 6, 15, 18, 3, 2]
    n = len(arr1)
    insertionSort_iterative(arr1)
    print("Sorted Array is:", end=" ")
    printArray(arr1, n)
