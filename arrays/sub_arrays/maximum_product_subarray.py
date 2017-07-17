

def maxProductSubarray(arr):
    max_ending_here, min_ending_here, max_prod = 1, 1, 1

    for i in range(len(arr)):

        if(arr[i] > 0):
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min(min_ending_here * arr[i], 1)

        elif(arr[i] < 0):
            temp = max_ending_here
            max_ending_here = max(min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]

        else:
            max_ending_here = 1
            min_ending_here = 1

        if(max_prod < max_ending_here):
            max_prod = max_ending_here

    return max_prod


if __name__ == "__main__":
    arrays = [[1, -2, -3, 0, 7, -8, -2]]

    for array in arrays:
        print(array, "-->", end=" ")
        print(maxProductSubarray(array))
