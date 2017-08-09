

def compress(s):
    new = ""
    count = 1

    for i in range(1, len(s)):
        if(s[i-1] == s[i]):
            count += 1
        else:
            new += s[i-1]
            new += str(count)
            count = 1

    new += s[len(s)-1]
    new += str(count)

    return new


if __name__ == "__main__":
    strings = ["aaabbbbcc", "abcdef", "aaaaa", "abbc", "geeksforgeeks"]
    for string in strings:
        print(compress(string))
