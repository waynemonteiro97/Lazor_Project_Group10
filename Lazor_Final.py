import time
import numpy as np
import math
import copy

def create_grid(board):
    length = 2 * len(board) + 1
    width = 2 * len(board[0]) + 1
    grid = []
    for i in range(length):
        grid.append([])
        for j in range(width):
            grid[i].append('x') 
    for i in range(len(board)):
        for j in range(len(board[0])):
            grid[2 * i + 1][2 * j + 1] = board[i][j]
    '''
    for y in grid:
        for x in y:
            print(x, end=' ')
        print()
    '''
    return grid


def read_bff(filename):
    grid = []
    A_blocks = 0
    B_blocks = 0
    C_blocks = 0
    lazor_ori = []
    hole = []
    bff_read = open(filename, "r").read()
    file_content = bff_read.strip().split("\n")

    for i in range(len(file_content)):
        if file_content[i] == "GRID START":
            a = i+1
            while file_content[a] != "GRID STOP":
                grid.append(file_content[a])
                a = a + 1
        if len(file_content[i]) == 3 and file_content[i][0] == "A":
            A_blocks = int(file_content[i][2])
        if len(file_content[i]) == 3 and file_content[i][0] == "B":
            B_blocks = int(file_content[i][2])
        if len(file_content[i]) == 3 and file_content[i][0] == "C":
            C_blocks = int(file_content[i][2])
        if len(file_content[i]) != 0 and file_content[i][0] == "L":
            strip_lazor = file_content[i].split(" ")
            for j in range(1, len(strip_lazor), 2):
                lazor_ori.append((int(strip_lazor[j]), int(strip_lazor[j+1])))

        if len(file_content[i]) != 0 and file_content[i][0] == "P":
            hole.append([int(file_content[i][2]), int(file_content[i][4])])
    updated_grid = [] 
    lazors = []
    for i in range(int(len(lazor_ori)/2)):
        lazors.append([lazor_ori[2*i], lazor_ori[2*i + 1]])
    for x in grid: 
        lists = x.split() 
        updated_grid.append(lists)
    return(updated_grid, A_blocks, B_blocks, C_blocks, lazors, hole)


def next_step(grid, pos, direc):
    x = pos[0]
    y = pos[1]
    if y % 2 == 0:
        '''
        If y is even then block lies above or below
        '''
        if grid[y + direc[1]][x].lower() == 'o' or grid[y + direc[1]][x].lower() == 'x':
            new_dir = direc
        elif grid[y + direc[1]][x].lower() == 'a':
            new_dir = [direc[0], -1 * direc[1]]
        elif grid[y + direc[1]][x].lower() == 'b':
            new_dir = []
        elif grid[y + direc[1]][x].lower() == 'c':
            direc1 = direc
            direc2 = [direc[0], -1 * direc[1]]
            new_dir = [direc1[0], direc1[1], direc2[0], direc2[1]]
    else:
        '''
        If y is odd the block is left or right
        '''
        if grid[y][x + direc[0]].lower() == 'o' or grid[y][x + direc[0]].lower() == 'x':
            new_dir = direc
        elif grid[y][x + direc[0]].lower() == 'a':
            new_dir = [-1 * direc[0], direc[1]]
        elif grid[y][x + direc[0]].lower() == 'b':
            new_dir = []
        elif grid[y][x + direc[0]].lower() == 'c':
            direc1 = direc
            direc2 = [-1 * direc[0], direc[1]]
            new_dir = [direc1[0], direc1[1], direc2[0], direc2[1]]

    return new_dir


def boundary_check(grid, pos, direc):
    x = pos[0]
    y = pos[1]
    y_max = len(grid) - 1
    x_max = len(grid[0]) - 1
    if x < 0 or x > x_max or y < 0 or y > y_max or (x + direc[0]) < 0 or (x + direc[0]) > x_max or (y + direc[1]) < 0 or (y + direc[1]) > y_max :
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
        n = len(stack_lazors)
        for i in range(len(stack_lazors)):
            lazor_pos = list(stack_lazors[i][-1][0])
            direc = list(stack_lazors[i][-1][1])
            if boundary_check(grid, lazor_pos, direc):
                break
            else:
                new_dir = next_step(grid, lazor_pos, direc)
                if len(new_dir) == 0:
                    stack_lazors[i].append([lazor_pos, direc])
                elif len(new_dir) == 2:
                    direc = new_dir
                    lazor_pos = [lazor_pos[0] + direc[0], lazor_pos[1] + direc[1]]
                    stack_lazors[i].append([lazor_pos, direc])
                else:
                    direc = new_dir
                    lazor_pos1 = [lazor_pos[0] + direc[0], lazor_pos[1] + direc[1]]
                    lazor_pos2 = [lazor_pos[0] + direc[2], lazor_pos[1] + direc[3]]
                    stack_lazors.append([[lazor_pos1, [direc[0], direc[1]]]])
                    stack_lazors[i].append([lazor_pos2, [direc[2], direc[3]]])
                    lazor_pos = lazor_pos2
            if lazor_pos in sinks:
                    sinks.remove(lazor_pos)
    # print(stack_lazors)
    if len(sinks) == 0:
        return True
    else:
        return False


def blocks(board, A_blocks, B_blocks, C_blocks, lazors, hole):
    movable_blocks=[]
    print(board)
    for x in board:
        for y in x :
            if y == 'o':
                movable_blocks.append(y)
    for i in range(A_blocks):
        movable_blocks[i] = 'A'
    for i in range(A_blocks, (A_blocks+B_blocks)):
        movable_blocks[i] = 'B'
    for i in range((A_blocks+B_blocks), (A_blocks+B_blocks+C_blocks)):
        movable_blocks[i] = 'C'
    MAX_BOARDS = math.factorial(len(movable_blocks))
    if A_blocks !=  0 :
        MAX_BOARDS = int(MAX_BOARDS / A_blocks)
    if B_blocks != 0:
        MAX_BOARDS = int(MAX_BOARDS / B_blocks)
    if C_blocks != 0:
        MAX_BOARDS = int(MAX_BOARDS / C_blocks)
    ITER_B = 0
    length=len(board)
    width=len(board[0])
    while ITER_B <= MAX_BOARDS:
        permut = list(np.random.permutation(movable_blocks))
        possible_board = copy.deepcopy(board)
        counter = 0
        for i in range(length):
            for j in range (width):
                if possible_board[i][j] == 'o':
                    possible_board[i][j] = permut[counter]
                    counter +=1
        grid = create_grid(possible_board)
        ITER_B += 1
        if lazor_path(grid, lazors, hole):
            print("Congo")
            print(grid)
            break

    
if __name__ == "__main__":
    grid, A_blocks, B_blocks, C_blocks, lazors, hole=read_bff("yarn_5.bff")
    print(lazors)
    print(hole)
    time_start = time.time()
    blocks(grid, A_blocks, B_blocks, C_blocks, lazors, hole)
    time_end = time.time()
    print('run time: %f seconds' %(time_end - time_start))