from collections import deque


def max_of_all_subarrays_of_size_k(arr, k):
    n = len(arr)
    i = 0
    qu = deque([])
    for i in range(k):
        while(len(qu) > 0 and arr[qu[-1]] <= arr[i]):
            qu.pop()
        qu.append(i)

    for i in range(i+1, n):
        print (arr[qu[0]], end=" ")

        while(len(qu) > 0 and qu[0] <= i-k):
            qu.popleft()

        while(len(qu) > 0 and arr[qu[-1]] <= arr[i]):
            qu.pop()
        qu.append(i)

    print (arr[qu[0]], end=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    max_of_all_subarrays_of_size_k(arr, k)
