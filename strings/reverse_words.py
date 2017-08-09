

def reverseRange(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverseWords(arr):
    n = len(arr)

    i = 0
    while(i < n):
        start = i
        while(i < n and arr[i] != ' ' and arr[i] != '\n'):
            end = i
            i += 1

        reverseRange(arr, start, end)
        i += 1

    reverseRange(arr, 0, n-1)

    print(''.join(arr))


if __name__ == "__main__":
    sentence = "Manikanta is a football player"
    array = list(sentence)

    reverseWords(array)
