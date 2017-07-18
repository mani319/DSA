"""
Consider a game where a player can score 3 or 5 or 10 points in a move.
Given a total score n, find number of ways to reach the given score.
"""


def numberOfWays(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(3, n+1):
        dp[i] += dp[i-3]
    for i in range(5, n+1):
        dp[i] += dp[i-5]
    for i in range(10, n+1):
        dp[i] += dp[i-10]

    return dp[n]


if __name__ == "__main__":
    n_values = [13, 20, 80, 100, 130, 200, 512, 1000]

    for n in n_values:
        print(numberOfWays(n))
