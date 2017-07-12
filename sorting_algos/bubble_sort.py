'''

Bubble Sort

'''


def bubbleSort_recursive(arr, n):
    if(n == 1):
        return

    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubbleSort_recursive(arr, n-1)


def bubbleSort_iterative(arr):
    n = len(arr)

    for i in range(n):
        flag = 0

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1

        if flag == 0:
            break


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 13]

    bubbleSort_iterative(arr)

    print ("Sorted array is:", end=" ")
    for i in range(len(arr)):
        print (arr[i], end=' ')
    print()

    arr1 = [64, 34, 25, 12, 22, 11, 90, 13]
    bubbleSort_recursive(arr1, len(arr1))

    print ("Sorted array is:", end=" ")
    for i in range(len(arr1)):
        print (arr1[i], end=' ')
