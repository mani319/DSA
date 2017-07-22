"""
Determine whether a given graph contains Hamiltonian Cycle or not.
If it contains, then print the path.

For example, a Hamiltonian Cycle in the following graph is {0, 1, 2, 4, 3, 0}.
There are more Hamiltonian Cycles in the graph like {0, 3, 4, 2, 1, 0}

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)-------(4)

And the following graph doesn’t contain any Hamiltonian Cycle.

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)      (4)
"""


def isSafe(graph, v, path, pos):
    # Current and last vertex in path are adjacent
    if(graph[path[pos-1]][v] == 0):
        return False

    # Current vertex is already in path
    for vertex in path:
        if(vertex == v):
            return False

    return True


def hamCycleUtil(graph, vertices, path, pos):
    if(pos == vertices):
        return (graph[path[pos-1]][path[0]] == 1)

    for v in range(1, vertices):
        if(isSafe(graph, v, path, pos)):
            path[pos] = v

            if(hamCycleUtil(graph, vertices, path, pos+1)):
                return True

            path[pos] = -1

    return False


def printSolution(path):
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])


def hamCycle(graph):
    vertices = len(graph)
    path = [-1]*vertices
    path[0] = 0

    pos = 1
    if(not hamCycleUtil(graph, vertices, path, pos)):
        print("No Solution")
        return False

    printSolution(path)
    return True


if __name__ == "__main__":
    """
      (0)--(1)--(2)
       |   / \   |
       |  /   \  |
       | /     \ |
      (3)-------(4)
    """
    graph1 = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
              [0, 1, 0, 0, 1], [1, 1, 0, 0, 1],
              [0, 1, 1, 1, 0]]
    hamCycle(graph1)

    """
      (0)--(1)--(2)
       |   / \   |
       |  /   \  |
       | /     \ |
      (3)       (4)
    """
    graph2 = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
              [0, 1, 0, 0, 1], [1, 1, 0, 0, 0],
              [0, 1, 1, 0, 0]]
    hamCycle(graph2)
