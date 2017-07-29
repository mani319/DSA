"""
Given a value V, if we want to make change for V Rs, and
we have infinite supply of each of the denominations in Indian currency,
i.e., we have infinite { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued notes,
what is the minimum number of coins and/or notes needed to make the change?

The idea is simple Greedy Algorithm.
Start from largest possible denomination and keep adding denominations
    while remaining value is greater than 0.
"""


def calcuateChange(denoms, val):
    res = []

    for i in range(len(denoms)-1, -1, -1):
        while(val >= denoms[i]):
            val -= denoms[i]
            res.append(denoms[i])

    return res


if __name__ == "__main__":
    denoms = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    val = 1788
    print(calcuateChange(denoms, val))
