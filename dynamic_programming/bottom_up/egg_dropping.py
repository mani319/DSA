"""

"""

import math


def egg_dropping(eggs, floors):
    dp = []
    for i in range(eggs+1):
        dp += [[math.inf]*(floors+1)]

    for i in range(eggs+1):
        dp[i][0] = 0
        dp[i][1] = 1

    for i in range(floors+1):
        dp[0][i] = 0
        dp[1][i] = i

    for i in range(2, eggs+1):
        for j in range(2, floors+1):
            for x in range(1, j+1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(res, dp[i][j])

    return dp[eggs][floors]


if __name__ == "__main__":
    eggs = 2
    floors = 100
    print(egg_dropping(eggs, floors))
