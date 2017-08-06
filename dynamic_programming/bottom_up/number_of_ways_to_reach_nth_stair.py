"""
Generalization of the number of ways to cover distance problem
How to count number of ways if the person can climb up to s stairs?
For example if s is 4,
    the person can climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.

We can write the recurrence as following.

   ways(n, s) = ways(n-1, s) + ways(n-2, s) + ... ways(n-s, s) 
"""


def noOfWays(n, s):
    dp = [0]*(n+1)

    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        j = 1
        while(j <= s and j <= i):
            dp[i] += dp[i-j]
            j += 1

    return dp[n]


if __name__ == "__main__":
    n, s = 4, 3
    print (noOfWays(n, s))
