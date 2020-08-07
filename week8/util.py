
def create_grid(grid):
	grid.append([0, 0, 0, 0])
	grid.append([0, 0, 0, 0])
	grid.append([0, 0, 0, 0])
	grid.append([0, 0, 0, 0])
	return grid


def print_grid(grid):
  print("+--------------------+")
  for row in range(4):

    print("|",end="")
    for col in range(4):
      if (grid[row][col] == 0):
        print("{0:<5}".format(" "), end="")
      else:
        print("{0:<5}".format(grid[row][col]), end="")
    print("|")
  print("+--------------------+")

def check_lost(grid):
    for i in range(len(grid)-1):
        for j in range(len(grid[0]) - 1):
            if grid[i][j] != grid[i+1][j] or grid[i][j+1] == grid[i][j]:
                return 'True'
            else:
                return 'False'

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                return 'True'
            else:
                return 'False'
    for k in range(len(grid)-1):
        if grid[len(grid)-1][k] != grid[len(grid)-1][k+1]:
            return 'True'
        else:
            return 'False'
    for j in range(len(grid)-1):
        if grid[j][len(grid)-1] != grid[j+1][len(grid)-1]:
            return 'True'
        else:
            return 'False'



def check_won(grid):
    for i in range(len(grid)):
        if grid[i] == 32:
            return 'True'
        else:
            return 'False'

def copy_grid(grid):
	grid = grid.copy()
	return grid


def grid_equal(grid1, grid2):
	if grid1 == grid2:
		return True
	else:
		return False
