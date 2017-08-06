"""
"""
import math


def rodCutting(price, n):
    dp = [0 for i in range(n+1)]

    for i in range(1, n+1):
        max_price = -math.inf
        for j in range(i):
            max_price = max(price[j] + dp[i-j-1], max_price)
        dp[i] = max_price

    return dp[n]


if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(price)

    print(rodCutting(price, size))
