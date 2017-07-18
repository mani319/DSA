'''
'''

Vertices = 4


def isSafe(graph, sol, vertex, color):
    # If any vertex is connected to 'v' and colred with 'color'
    for i in range(Vertices):
        if(graph[vertex][i] == 1 and sol[i] == color):
            return False

    return True


def mColoringUtil(graph, m, sol, vertex):
    # If all vertices completed
    if(vertex == Vertices):
        return True

    # Check with each color
    for color in range(1, m+1):
        if(isSafe(graph, sol, vertex, color)):
            sol[vertex] = color

            if(mColoringUtil(graph, m, sol, vertex+1)):
                return True

            sol[vertex] = 0

    return False


def mColoring(graph, m):
    sol = [0]*Vertices
    vertex = 0

    if(mColoringUtil(graph, m, sol, vertex)):
        print(sol)
    else:
        print("Cannot be colored with %d colors", m)


if __name__ == "__main__":
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    m = 3

    mColoring(graph, m)
