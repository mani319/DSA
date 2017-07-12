'''
*** Find the minimum distance between two numbers ***
Given an unsorted array arr[] and two numbers x and y.
find the minimum distance between x and y in arr[].
The array might also contain duplicates.
You may assume that both x and y are different and present in arr[]

Eg:
Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
Output: Minimum distance between 3 and 6 is 4.

Approach:http://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/

'''


def min_dist_btw_two_nums(arr, x, y):
    n = len(arr)
    min_len = n

    # Find the first occurence of any of the two numbers (x or y)
    # and store the index of this occurence in start
    i = 0
    while(i < n):
        if(arr[i] == x or arr[i] == y):
            start = i
            break

        i += 1

    # Traverse after the first occurence
    while(i < n):
        if(arr[i] == x or arr[i] == y):
            # check if current element and prev element are different
            if(arr[i] != arr[start]):
                min_len = min(min_len, i-start)

            start = i

        i += 1

    return min_len


if __name__ == "__main__":
    arrays = [[1, 2],
              [3, 4, 5],
              [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3],
              [2, 5, 3, 5, 4, 4, 2, 3],
              [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]]
    x_values = [1,
                3,
                3,
                3,
                3]
    y_values = [2,
                5,
                6,
                2,
                6]

    for i in range(len(arrays)):
        print(arrays[i], "x:", x_values[i], "y:", y_values[i], "-->",
              min_dist_btw_two_nums(arrays[i], x_values[i], y_values[i]))
