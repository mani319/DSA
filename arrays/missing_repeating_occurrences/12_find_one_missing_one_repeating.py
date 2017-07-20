"""
"""


def xor_method(arr):
    n = len(arr)

    xor = 0
    for i in range(n):
        xor ^= arr[i] ^ (i+1)

    set_bit = xor & ~(xor-1)

    x, y = 0, 0
    for i in range(n):
        if(set_bit & arr[i]):
            x ^= arr[i]
        else:
            y ^= arr[i]

    for i in range(1, n+1):
        if(set_bit & i):
            x ^= i
        else:
            y ^= i

    flag = 0
    for i in range(n):
        if(arr[i] == x):
            flag = 1

    if(flag == 1):
        print("Repeating Element is:", x, end=" ")
        print(", Missing Element is:", y)
    else:
        print("Repeating Element is:", y, end=" ")
        print(", Missing Element is:", x)


def array_modify(arr):
    n = len(arr)

    print("Repeating Element is:", end=" ")
    for i in range(n):
        if(arr[abs(arr[i])-1] > 0):
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print(abs(arr[i]), end=" ")

    print(", Missing Element is:", end=" ")
    for i in range(n):
        if(arr[i] > 0):
            print(i+1)


def find_missing_and_repeating(arr):
    xor_method(arr)
    array_modify(arr)
    # sum_product(arr)


if __name__ == "__main__":
    arrays = [[1, 2, 3, 3, 5],
              [1, 6, 3, 4, 7, 8, 5, 6],
              [1, 4, 3, 4]]

    for array in arrays:
        print(array)
        find_missing_and_repeating(array)
        print("-----------------------------------------------------------")
