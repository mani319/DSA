'''

Given a string consisting of opening and closing parenthesis.
Find length of the longest valid parenthesis substring.

Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()()

Input:  ()(()))))
Output: 6
Explanation:  ()(())

Approach:http://www.geeksforgeeks.org/length-of-the-longest-valid-substring/

'''


def maxValidParentheses(s):
    n = len(s)

    st = []
    st.append(-1)   # Imp step
    result = 0

    for i in range(n):
        if(s[i] == '('):
            st.append(i)    # push index
        else:
            st.pop()        # returns -1 if stack is empty

            if(len(st) > 0):
                result = max(i - st[len(st)-1], result)
            else:
                st.append(i)

    return result


if __name__ == "__main__":
    strings = ["((()()",
               "()(()))))",
               ")()())",
               ")((()"]

    for string in strings:
        print(maxValidParentheses(string))
