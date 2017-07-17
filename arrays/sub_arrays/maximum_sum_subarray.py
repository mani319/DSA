

def maxSumSubarray(arr):
    max_ending_here, max_sum = 0, 0

    curr_start, start, end = 0, 0, 0
    for i in range(len(arr)):
        max_ending_here += arr[i]

        if(max_sum < max_ending_here):
            max_sum = max_ending_here
            start = curr_start
            end = i

        if(max_ending_here < 0):
            max_ending_here = 0
            curr_start = i+1

    print([start, end], end=" ")
    return max_sum


if __name__ == "__main__":
    arrays = [[-2, -3, 4, -1, -2, 0, 1, 5, -3]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(maxSumSubarray(array))
