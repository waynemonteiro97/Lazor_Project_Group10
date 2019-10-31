'''
Lazor Solver
Prabhjot Kaur Luthra
'''


def next_step(grid, pos, direc):
    x = pos[0]
    y = pos[1]
    if x % 2 == 0:
        '''
        If x is even then block lies above or below
        '''
        if grid[x + direc[0]][y] == 'o' or grid[x + direc[0]][y] == 'x':
            new_dir = direc
        elif grid[x + direc[0]][y] == 'a':
            new_dir = [-1 * direc[0], direc[1]]
        elif grid[x + direc[0]][y] == 'b':
            new_dir = []
        elif grid[x + direc[0]][y] == 'c':
            direc1 = direc
            direc2 = [-1 * direc[0], direc[1]]
            new_dir = [direc1[0], direc1[1], direc2[0], direc2[1]]
    else:
        '''
        If x is odd the block is left or right
        '''
        if grid[x][y + direc[1]] == 'o' or grid[x][y + direc[1]] == 'x':
            new_dir = direc
        elif grid[x][y + direc[1]] == 'a':
            new_dir = [direc[0], -1 * direc[1]]
        elif grid[x][y + direc[1]] == 'b':
            new_dir = []
        elif grid[x][y + direc[1]] == 'c':
            direc1 = direc
            direc2 = [direc[0], -1 * direc[1]]
            new_dir = [direc1[0], direc1[1], direc2[0], direc2[1]]

    return new_dir


def boundary_check(grid, pos):
    x = pos[0]
    y = pos[1]
    x_max = len(grid)
    y_max = len(grid[0])
    if x < 0 or x > x_max or y < 0 or y >= y_max:
        return True
    else:
        return False


def lazor_path(grid, lazors, sinks):
    # list of all lazors and and each lazor list has its path
    stack_lazors = []
    for i in range(len(lazors)):
        stack_lazors.append([lazors[i]])
    # lazor_pos = stack_lazors[-1]
    ITER = 0
    MAX_ITER = 1000
    while len(sinks) != 0 and ITER <= MAX_ITER:
        # print('Here')
        ITER += 1
        for i in range(len(stack_lazors)):
            lazor_pos = list(stack_lazors[i][-1][0])
            direc = list(stack_lazors[i][-1][1])
            # print(lazor_pos)
            if boundary_check(grid, lazor_pos):
                break
            else:
                new_dir = next_step(grid, lazor_pos, direc)
                if len(new_dir) == 0:
                    stack_lazors[i].append([])
                elif len(new_dir) == 2:
                    direc = new_dir
                    lazor_pos = [lazor_pos[0] + direc[0], lazor_pos[1] + direc[1]]
                    stack_lazors[i].append([lazor_pos, direc])
                else:
                    direc1 = new_dir[0]
                    direc2 = new_dir[1]
                    lazor_pos1 = [lazor_pos[0] + direc1[0], lazor_pos[1] + direc1[1]]
                    lazor_pos2 = [lazor_pos[0] + direc2[0], lazor_pos[1] + direc2[1]]
                    stack_lazors.append([lazor_pos1])
                    stack_lazors[i].append(lazor_pos2)
                    lazor_pos = lazor_pos2
            n = len(sinks)
            for i in range(n):
                if lazor_pos == sinks[i]:
                    sinks.remove(lazor_pos)
    print(stack_lazors)
    if len(sinks) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    grid = []
    for i in range(7):
        grid.append([])
        for j in range(7):
            grid[i].append('x')
    for i in range(3):
        for j in range(3):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[3][1] = 'a'
    grid[1][5] = 'a'
    grid[3][5] = 'a'
    grid[5][3] = 'a'
    print(grid)
    origin = (0,3)
    direc = (1, 1)
    hole = [[1,2]]
    if lazor_path(grid, [[origin, direc]], hole):
        print("Congo")
    else:
        print("Try again")

