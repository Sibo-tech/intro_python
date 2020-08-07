def push_up(grid):
    grid = grid
    i=0
    for j in range(0,4):
        if grid[i][j]!=0 or grid[i+1][j]!=0 or grid[i+2][j]!=0 or grid[i+3][j]!=0:
            if grid[i][j]==0:
                while grid[i][j]==0:
                    grid[i][j] =grid[i+1][j]
                    grid[i+1][j] = grid[i+2][j]
                    grid[i+2][j] = grid[i+3][j]
                    grid[i+3][j] = 0
            if grid[i + 1][j] == 0 and (grid[i + 2][j] != 0 or grid[i + 3][j] != 0):
                while grid[i+1][j]==0:
                    grid[i+1][j] = grid[i+2][j]
                    grid[i+2][j] = grid[i+3][j]
                    grid[i+3][j] = 0
            if grid[i + 2][j] == 0 and (grid[i + 3][j] != 0):
                while grid[i+2][j]:
                    grid[i+2][j] = grid[i+3][j]
                    grid[i+3][j] = 0
    i=0
    for j in range(0,4):
        if grid[i][j] == grid[i+1][j]:
            grid[i][j] = grid[i][j]+grid[i+1][j]
            grid[i + 1][j] = grid[i + 2][j]
            grid[i + 2][j] = grid[i + 3][j]
            grid[i + 3][j] = 0
        if grid[i + 1][j] == grid[i + 2][j]:
            grid[i + 1][j] = grid[i + 1][j]+grid[i+2][j]
            grid[i + 2][j] = grid[i + 3][j]
            grid[i + 3][j]=0
        if  grid[i + 2][j] == grid[i + 3][j]:
            grid[i + 2][j] = grid[i + 2][j]+grid[i + 3][j]
            grid[i + 3][j]=0
    return grid

def push_down(grid):
    i = 0
    for j in range(0, 4):
        if grid[i][j] != 0 or grid[i + 1][j] != 0 or grid[i + 2][j] != 0 or grid[i + 3][j] != 0:
            if grid[i + 3][j] == 0:
                while grid[i + 3][j] == 0:
                    grid[i + 3][j] = grid[i + 2][j]
                    grid[i + 2][j] = grid[i + 1][j]
                    grid[i + 1][j] = grid[i][j]
                    grid[i][j] = 0
            if grid[i + 2][j] == 0 and (grid[i + 1][j] != 0 or grid[i][j] != 0):
                while grid[i + 2][j] == 0:
                    grid[i + 2][j] = grid[i + 1][j]
                    grid[i + 1][j] = grid[i][j]
                    grid[i][j] = 0

            if grid[i + 1][j] == 0 and grid[i][j] != 0:
                while grid[i + 1][j] == 0:
                    grid[i + 1][j] = grid[i][j]
                    grid[i][j] = 0
    i = 0
    for j in range(0, 4):
        if grid[i + 3][j] == grid[i + 2][j]:
            grid[i + 3][j] = grid[i + 3][j] + grid[i + 2][j]
            grid[i + 2][j] = grid[i + 1][j]
            grid[i + 1][j] = grid[i][j]
            grid[i][j] = 0
        if grid[i + 2][j] == grid[i + 1][j]:
            grid[i + 2][j] = grid[i + 2][j] + grid[i + 1][j]
            grid[i + 1][j] = grid[i][j]
            grid[i][j] = 0
        if grid[i + 1][j] == grid[i][j]:
            grid[i + 1][j] = grid[i + 1][j] + grid[i][j]
            grid[i][j] = 0
    return grid


def push_left(grid):
    j = 0
    for i in range(0, 4):
        if grid[i][j] != 0 or grid[i][j + 1] != 0 or grid[i][j + 2] != 0 or grid[i][j + 3] != 0:
            if grid[i][j] == 0:
                while grid[i][j] == 0:
                    grid[i][j] = grid[i][j + 1]
                    grid[i][j + 1] = grid[i][j + 2]
                    grid[i][j + 2] = grid[i][j + 3]
                    grid[i][j + 3] = 0
            if grid[i][j + 1] == 0 and (grid[i][j + 2] != 0 or grid[i][j + 3] != 0):
                while grid[i][j + 1] == 0:
                    grid[i][j + 1] = grid[i][j + 2]
                    grid[i][j + 2] = grid[i][j + 3]
                    grid[i][j + 3] = 0
            if grid[i][j + 2] == 0 and (grid[i][j + 3] != 0):
                while grid[i][j + 2] == 0:
                    grid[i][j + 2] = grid[i][j + 3]
                    grid[i][j + 3] = 0
    j = 0
    for i in range(0, 4):
        if grid[i][j] == grid[i][j + 1]:
            grid[i][j] = grid[i][j] + grid[i][j + 1]
            grid[i][j + 1] = grid[i][j + 2]
            grid[i][j + 2] = grid[i][j + 3]
            grid[i][j + 3] = 0
        if grid[i][j + 1] == grid[i][j + 2]:
            grid[i][j + 1] = grid[i][j + 1] + grid[i][j + 2]
            grid[i][j + 2] = grid[i][j + 3]
            grid[i][j + 3] = 0
        if grid[i][j + 2] == grid[i][j + 3]:
            grid[i][j + 2] = grid[i][j + 2] + grid[i][j + 3]
            grid[i][j + 3] = 0
    return grid


def push_right(grid):
    j = 0
    for i in range(0, 4):
        if grid[i][j] != 0 or grid[i][j + 1] != 0 or grid[i][j + 2] != 0 or grid[i][j + 3] != 0:
            if grid[i][j + 3] == 0:
                while grid[i][j + 3] == 0:
                    grid[i][j + 3] = grid[i][j + 2]
                    grid[i][j + 2] = grid[i][j + 1]
                    grid[i][j + 1] = grid[i][j]
                    grid[i][j] = 0
            if grid[i][j + 2] == 0 and (grid[i][j + 1] != 0 or grid[i][j] != 0):
                while grid[i][j + 2] == 0:
                    grid[i][j + 2] = grid[i][j + 1]
                    grid[i][j + 1] = grid[i][j]
                    grid[i][j] = 0
            if grid[i][j + 1] == 0 and grid[i][j] != 0:
                while grid[i][j + 1] == 0:
                    grid[i][j + 1] = grid[i][j]
                    grid[i][j] = 0
    j = 0
    for i in range(0, 4):
        if grid[i][j + 3] == grid[i][j + 2]:
            grid[i][j + 3] = grid[i][j + 3] + grid[i][j + 2]
            grid[i][j + 2] = grid[i][j + 1]
            grid[i][j + 1] = grid[i][j]
            grid[i][j] = 0
        if grid[i][j + 2] == grid[i][j + 1]:
            grid[i][j + 2] = grid[i][j + 2] + grid[i][j + 1]
            grid[i][j + 1] = grid[i][j]
            grid[i][j] = 0
        if grid[i][j + 1] == grid[i][j]:
            grid[i][j + 1] = grid[i][j + 1] + grid[i][j]
            grid[i][j] = 0
    return grid




