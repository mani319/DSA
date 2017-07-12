'''
A Maze is given as N*N binary matrix of blocks where
    source block is the upper left most block i.e., maze[0][0] and
    destination block is lower rightmost block i.e., maze[N-1][N-1].
A rat starts from source and has to reach destination.
The rat can move only in two directions: forward and down.
In the maze matrix,
    0 means the block is dead end and
    1 means the block can be used in the path from source to destination.
'''

N = 4


def isSafe(maze, x, y):
    # check x bounds
    if(x < 0 or x >= N):
        return False

    # check y bounds
    if(y < 0 or y >= N):
        return False

    # check whether cell is dead
    if(maze[x][y] == 0):
        return False

    return True


def rat_maze_util(maze, path, x, y):
    if(x == N-1 and y == N-1):
        path[x][y] = 1
        return True

    if(isSafe(maze, x, y)):
        path[x][y] = 1

        # Go down and check
        if(rat_maze_util(maze, path, x+1, y)):
            return True

        # Go right and check
        if(rat_maze_util(maze, path, x, y+1)):
            return True

        path[x][y] = 0

    return False


def rat_maze(maze):
    x = 0
    y = 0
    path = []
    for row in range(N):
        path += [[0]*N]

    if(rat_maze_util(maze, path, x, y)):
        print("Maze Solution is: ")
        for row in range(N):
            print(path[row])
    else:
        print("No Solution for Maze")


if __name__ == "__main__":
    maze = [[1, 1, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 0, 1]]
    rat_maze(maze)
