"""
Given a cost matrix cost[][] and a position (m, n) in cost[][],
Write function that returns cost of minimum cost path to reach (m,n) from (0,0)
Each cell of the matrix represents a cost to traverse through that cell.
You can only traverse down, right and diagonally lower cells from a given cell,
i.e.,
from a cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed
"""


def minCost(costs, row, col):
    dp = []
    for i in range(row+1):
        dp += [[0]*(col+1)]

    dp[0][0] = costs[0][0]

    for i in range(1, row+1):
        dp[i][0] = dp[i-1][0] + costs[i][0]

    for i in range(1, col+1):
        dp[0][i] = dp[0][i-1] + costs[0][i]

    for i in range(1, row+1):
        for j in range(1, col+1):
            dp[i][j] = costs[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[row][col]


if __name__ == "__main__":
    costs = [[1, 2, 3],
             [4, 8, 2],
             [1, 5, 3]]

    print(minCost(costs, 2, 2))
