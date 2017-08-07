"""
"""


def minCashFlowUtil(balances):
    mini_bal = min(balances)
    maxi_bal = max(balances)
    if(mini_bal == 0 and maxi_bal == 0):
        return

    mini_bal_index = balances.index(mini_bal)
    maxi_bal_index = balances.index(maxi_bal)

    balances[mini_bal_index] -= mini_bal
    balances[maxi_bal_index] += mini_bal

    print ("Person", mini_bal_index, "pays",
           -mini_bal, "to Person", maxi_bal_index)

    minCashFlowUtil(balances)


def minCashFlow(gr, n):
    balances = [0]*n

    for i in range(n):
        for j in range(n):
            balances[i] += gr[j][i] - gr[i][j]

    minCashFlowUtil(balances)


if __name__ == "__main__":
    graph = [[0, 1000, 2000],
             [0, 0, 5000],
             [0, 0, 0]]

    n = len(graph)

    minCashFlow(graph, n)
