'''



'''


def opening_brace(i):
    return (i is '[' or
            i is '{' or
            i is '(')


def closing_brace(i):
    return (i is ']' or
            i is '}' or
            i is ')')


def matching_braces(i, j):
    return ((i is '[' and j is ']') or
            (i is '{' and j is '}') or
            (i is '(' and j is ')'))


def balanced_or_not(s):
    st = []
    for i in s:
        if(opening_brace(i)):
            st.append(i)
        elif(closing_brace(i)):
            if(len(st) == 0 or not matching_braces(st.pop(), i)):
                return False
        else:
            pass

    if(len(st) == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    strings = ["({[]})",
               "([)]",
               "{[(])}",
               "{[()()]()}",
               "[(])"]

    for s in strings:
        if(balanced_or_not(s)):
            print ("YES")
        else:
            print("NO")
