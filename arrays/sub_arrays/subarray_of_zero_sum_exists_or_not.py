

def subarray_of_zero_sum_exists_or_not(arr):
    n = len(arr)
    curr_sum = 0

    hash_map = {}
    for i in range(n):
        curr_sum += arr[i]

        if(curr_sum == 0):
            return True

        if(curr_sum in hash_map.keys()):
            return True
        else:
            hash_map[curr_sum] = i

    return False


if __name__ == "__main__":
    arrays = [[10, 2, -2, -20, 10],
              [1, 4, 20, 3, 10, 5],
              [-10, 0, 2, -2, -20, 10],
              [1, 4, 0, 0, 3, 10, 5],
              [1, 4]]

    for i in range(len(arrays)):
        print(arrays[i], "sum:", 0, "-->", end=" ")
        if(subarray_of_zero_sum_exists_or_not(arrays[i])):
            print("Exists")
        else:
            print("Doesn't Exist")
