

def maxDiffLargerOnRight(arr):
    n = len(arr)

    max_diff = arr[1]-arr[0]
    min_element = arr[0]
    for i in range(1, n):
        if(arr[i]-min_element > max_diff):
            max_diff = arr[i]-min_element

        if(arr[i] < min_element):
            min_element = arr[i]

    return max_diff


if __name__ == "__main__":
    arrays = [[1, 2, 6, 80, 100],
              [80, 2, 6, 3, 100],
              [1, 2, 90, 10, 110],
              [2, 3, 10, 6, 4, 8, 1],
              [7, 9, 5, 6, 3, 2]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(maxDiffLargerOnRight(array))
