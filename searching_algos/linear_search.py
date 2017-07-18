"""
Pass any type of array
"""


def linearSearch(arr, key):
    n = len(arr)

    for i in range(n):
        if(arr[i] == key):
            return i

    return -1


if __name__ == "__main__":
    arrays = [[5, 6, 7, 8, 9, 10, 1, 2, 3],
              [5, 6, 7, 8, 9, 10, 1, 2, 3],
              [5, 6, 7, 8, 9, 10, 1, 2, 3],
              [5, 6, 7, 8, 9, 10, 1, 2, 3]]
    keys = [5, 8, 3, 100]

    for i in range(len(arrays)):
        print(arrays[i], "key:", keys[i], "-->", "index:", end=" ")
        print(linearSearch(arrays[i], keys[i]))
