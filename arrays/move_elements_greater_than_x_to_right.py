'''
'''


def move_elements_greater_than_x_to_right(arr, x):
    n = len(arr)

    i, j = 0, n-1
    while(i < j):
        if(arr[i] > x):
            if(arr[j] <= x):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j -= 1
        else:
            i += 1


if __name__ == "__main__":
    array = [11, 10, 13, 2, 3, 14, 0, 12, 1, 8, 10, 4, 6]
    x = 10
    move_elements_greater_than_x_to_right(array, x)
    print(array)
