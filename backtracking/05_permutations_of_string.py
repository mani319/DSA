"""
Print all permutations of given string
"""


def permutations_util(s, l, r):
    if(l == r):
        print(''.join(s))
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]
            permutations_util(s, l+1, r)
            s[l], s[i] = s[i], s[l]


def permutations(str):
    s = list(str)
    print(s)
    n = len(s)
    permutations_util(s, 0, n-1)


if __name__ == "__main__":
    string = "mani"
    permutations(string)
