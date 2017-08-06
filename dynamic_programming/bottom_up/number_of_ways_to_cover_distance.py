"""
Given a distance 'dist',
count total number of ways to cover the distance with 1, 2 and 3 steps.

Examples:

Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7
"""


def noOfWays(dist):
    dp = [0]*(dist+1)

    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, dist+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[dist]


if __name__ == "__main__":
    dist = 3
    print (noOfWays(dist))
