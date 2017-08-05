"""
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS_Util(self, start, visited):
        stack = []

        visited[start] = True
        stack.append(start)

        while(stack):
            vert = stack.pop()
            print (vert, end=" ")

            for i in self.graph[vert]:
                if(not visited[i]):
                    visited[i] = True
                    stack.append(i)

    def DFS(self):
        visited = [False] * len(self.graph)

        for i in range(len(self.graph)):
            if(not visited[i]):
                self.DFS_Util(i, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 5)

    g.DFS()
