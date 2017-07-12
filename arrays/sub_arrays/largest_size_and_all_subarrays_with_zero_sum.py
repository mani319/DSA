

def all_subarrays_with_zero_sum(arr):
    n = len(arr)
    curr_sum = 0

    hash_map = {}
    result = []
    largest = 0
    for i in range(n):
        curr_sum += arr[i]

        if(curr_sum == 0):
            result.append([0, i])
            largest = i + 1

        if(curr_sum in hash_map.keys()):
            starts = hash_map[curr_sum]
            for j in range(len(starts)):
                result.append([starts[j]+1, i])
                largest = max(i-starts[j], largest)
        else:
            hash_map[curr_sum] = []

        hash_map[curr_sum].append(i)

    return result, largest


if __name__ == "__main__":
    arrays = [[6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7],
              [1, 4, 20, 3, 10, 5],
              [10, 2, 4, -2, -20, -4, 10],
              [1, 4, 0, 0, -1, 1, 3, 10, 5],
              [1, 4]]

    for i in range(len(arrays)):
        print(arrays[i], "sum:", 0, "-->",
              all_subarrays_with_zero_sum(arrays[i]))
