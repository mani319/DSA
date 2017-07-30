"""
Given a sorted array of positive integers, rearrange the array alternately
i.e first element should be the maximum value, second minimum value,
    third-second max, fourth-second min and so on.

Examples:

Input  : arr[] = {1, 2, 3, 4, 5, 6, 7}
Output : arr[] = {7, 1, 6, 2, 5, 3, 4}

Input  : arr[] = {1, 2, 3, 4, 5, 6}
Output : arr[] = {6, 1, 5, 2, 4, 3}

Method1:http://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/
Method2:http://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/
"""


def rearrange1(arr):
    '''
    O(n) time, O(n) space
    '''
    n = len(arr)
    new = []

    i, j = 0, n-1
    while(i <= j):
        new.append(arr[j])
        if(i != j):
            new.append(arr[i])
            i += 1
        j -= 1

    # Copy new elements to original array
    for i in range(n):
        arr[i] = new[i]


def rearrange2(arr):
    '''
    O(n) time and O(1) space - open link Method2 for complete explanation
    '''
    n = len(arr)

    max_index, min_index = n-1, 0
    max_plus_one = arr[n-1] + 1
    for i in range(n):
        if(i & 1):
            arr[i] += (arr[min_index] % max_plus_one) * max_plus_one
            min_index += 1
        else:
            arr[i] += (arr[max_index] % max_plus_one) * max_plus_one
            max_index -= 1

    # Get the new elements from the array values
    for i in range(n):
        arr[i] = arr[i] // max_plus_one


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    rearrange2(array)
    print(array)
