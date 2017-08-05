"""
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS_Util(self, start, visited):
        queue = []

        visited[start] = True
        queue.append(start)

        while(queue):
            vert = queue.pop(0)
            print (vert, end=" ")

            for i in self.graph[vert]:
                if(not visited[i]):
                    visited[i] = True
                    queue.append(i)

    def BFS(self):
        visited = [False] * len(self.graph)

        for i in range(len(self.graph)):
            if(not visited[i]):
                self.BFS_Util(i, visited)


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

    g.BFS()
