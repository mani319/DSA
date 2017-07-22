

def all_subarrays_with_given_sum(arr, given_sum):
    n = len(arr)
    curr_sum = 0

    hash_map = {}
    result = []
    largest = 0
    for i in range(n):
        curr_sum += arr[i]

        if(curr_sum == given_sum):
            result.append([0, i])
            largest = i + 1

        if((curr_sum - given_sum) in hash_map.keys()):
            starts = hash_map[curr_sum - given_sum]
            for j in range(len(starts)):
                result.append([starts[j]+1, i])
                largest = max(i-starts[j], largest)

        try:
            hash_map[curr_sum].append(i)
        except KeyError:
            hash_map[curr_sum] = [i]

    return result, largest


if __name__ == "__main__":
    arrays = [[10, 2, -2, -20, 10],
              [1, 4, 20, 3, 10, 5],
              [-10, 0, 2, -2, -20, 10],
              [1, 4, 0, 0, 3, 7, -7, 10, 5],
              [1, 4]]
    given_sum = [-10,
                 33,
                 20,
                 7,
                 0]

    for i in range(len(arrays)):
        print(arrays[i], "sum:", given_sum[i], "-->",
              all_subarrays_with_given_sum(arrays[i], given_sum[i]))
