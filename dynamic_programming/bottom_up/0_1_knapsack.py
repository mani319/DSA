"""
"""


def knapSack_0_1(W, wt, val, n):
    dp = []
    for i in range(n+1):
        dp += [[0]*(W+1)]

    for i in range(n+1):
        for w in range(W+1):
            if(i == 0 or w == 0):
                dp[i][w] = 0
            elif(w >= wt[i-1]):
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapSack_0_1(W, wt, val, n))
