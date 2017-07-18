"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
"""


def method_1(arr, d):
    """
    Using auxilary array of size d
    Uses O(d) extra space. Time Complexity: O(n)
    """
    n = len(arr)

    temp = [0]*d
    for i in range(d):
        temp[i] = arr[i]

    for i in range(n-d):
        arr[i] = arr[d+i]

    for i in range(d):
        arr[i+n-d] = temp[i]


def method_2(arr, d):
    """
    Rotate one by one element
    Time Complexity: O(n*d). Space: O(1)
    """
    n = len(arr)

    for i in range(d):
        temp = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]

        arr[n-1] = temp


def reverse(arr, left, right):
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def method_3(arr, d):
    """
    Steps:
    1. Reverse 0 to d-1
    2. Reverse d to n-1
    3. Reverse 0 to n-1
    Time Complexity: O(n) Space Complexity: O(1) Traversals: 2
    """
    n = len(arr)

    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)


def gcd(a, b):
    if(b == 0):
        return a

    return gcd(b, a % b)


def method_4(arr, d):
    """
    GCD Method
    Time Complexity: O(n) Space Complexity: O(1) Traversals: 1
    """
    n = len(arr)
    moves = gcd(d, n)

    for i in range(moves):
        j = i
        temp = arr[j]

        while(True):
            k = (j + d) % n
            if(k == i):
                break

            arr[j] = arr[k]
            j = k

        arr[j] = temp


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    method_1(array, d)
    print(array)

    array = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    method_2(array, d)
    print(array)

    array = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    method_3(array, d)
    print(array)

    array = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    method_4(array, d)
    print(array)
