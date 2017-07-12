'''

Given an array of distinct integers.
Find length of the longest subarray which contains numbers that can be
    arranged in a continuous sequence.

'''


def largest_subarray_with_contiguous_sequence_distinct_elements(arr):
    n = len(arr)
    max_len = 0

    for i in range(n-1):
        maxi = arr[i]
        mini = arr[i]

        for j in range(i+1, n):
            maxi = max(arr[j], maxi)
            mini = min(arr[j], mini)

            if(maxi-mini == j-i):
                max_len = max(maxi-mini+1, max_len)

    return max_len


'''

Given an array of integers.
find length of the longest subarray which contains numbers that can be
    arranged in a continuous sequence.

In the previous function, we have discussed a solution that assumes that
    elements in given array are distinct.
Here we discuss a solution that works even if the input array has duplicates.

'''


def largest_subarray_with_contiguous_sequence_duplicate_elements(arr):
    n = len(arr)
    max_len = 0

    for i in range(n-1):
        maxi = arr[i]
        mini = arr[i]

        hash_map = {}
        hash_map[arr[i]] = True

        for j in range(i+1, n):
            if(arr[j] in hash_map.keys()):
                break

            hash_map[arr[j]] = True

            maxi = max(arr[j], maxi)
            mini = min(arr[j], mini)
            if(maxi-mini == j-i):
                max_len = max(maxi-mini+1, max_len)

    return max_len


if __name__ == "__main__":
    arrays = [[10, 12, 11],
              [14, 12, 11, 20],
              [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]]
    for a in arrays:
        print(a, "-->",
              largest_subarray_with_contiguous_sequence_distinct_elements(a))

    print ("-----------------------------------------------------------")

    arrays1 = [[12, 14, 12],
               [10, 12, 12, 10, 10, 11, 10, 13, 13, 15, 14],
               [12, 11, 10, 10, 14, 10, 10, 13],
               []]
    for a1 in arrays1:
        print(a1, "--->",
              largest_subarray_with_contiguous_sequence_duplicate_elements(a1))
