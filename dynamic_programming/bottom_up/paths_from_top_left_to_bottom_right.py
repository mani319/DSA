"""
The problem is to count all the possible paths from top left to bottom right
    of a mXn matrix.
Constraints:
From each cell you can either move only to right or down
"""


def numberOfPaths(rows, cols):
    dp = []
    for i in range(rows):
        dp += [[0]*(cols)]

    for i in range(rows):
        dp[i][0] = 1

    for i in range(cols):
        dp[0][i] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[rows-1][cols-1]


if __name__ == "__main__":
    rows = 3
    cols = 3
    print(numberOfPaths(rows, cols))
