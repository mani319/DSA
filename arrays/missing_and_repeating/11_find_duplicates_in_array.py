'''

Given an array of n elements which contains elements from 0 to n-1,
with any of these numbers appearing any number of times.
Find these repeating numbers in O(n) and using only constant memory space.

Method1:http://www.geeksforgeeks.org/?p=9755
Method2:http://www.geeksforgeeks.org/duplicates-array-using-o1-extra-space-set-2/

'''


def find_duplicates_constant_space_method_1(arr):
    '''
        *** Doesn't work for all inputs ***
    '''
    n = len(arr)
    duplicates = []

    for i in range(n):
        if(arr[abs(arr[i])] >= 0):
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            duplicates.append(abs(arr[i]))

    return duplicates


def find_duplicates_constant_space_method_2(arr):
    '''
    Better Method and works for all the inputs
    '''
    n = len(arr)
    duplicates = []

    for i in range(n):
        index = arr[i] % n
        arr[index] += n

    for i in range(n):
        if((arr[i]//n) > 1):
            duplicates.append(i)

    return duplicates


if __name__ == "__main__":
    arrays = [[1, 2, 3, 1, 3, 6, 6],
              [1, 2, 3, 1, 3, 6, 6, 6, 3]]

    for array in arrays:
        print(array, "-->", end = " ")
        print(find_duplicates_constant_space_method_1(array))

    print("-------------------------------------------------------")

    arrays1 = [[1, 2, 3, 1, 3, 6, 6],
               [1, 2, 3, 1, 3, 6, 6, 6, 3]]

    for array1 in arrays1:
        print(array1, "-->", end = " ")
        print(find_duplicates_constant_space_method_2(array1))
