# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:49:16 2019

@author: Wayne Monteiro
"""

def next_step(grid, pos, direc):
    x = pos[0]
    y = pos[1]
    if y % 2 == 0:
        '''
        If y is even then block lies above or below
        '''
        if grid[y + direc[1]][x] == 'o' or grid[y + direc[1]][x] == 'x':
            new_dir = direc
        elif grid[y + direc[1]][x] == 'a':
            new_dir = [direc[0], -1 * direc[1]]
        elif grid[y + direc[1]][x] == 'b':
            new_dir = []
        elif grid[y + direc[1]][x] == 'c':
            direc1 = direc
            direc2 = [direc[0], -1 * direc[1]]
            new_dir = [direc1[0], direc1[1], direc2[0], direc2[1]]
    else:
        '''
        If y is odd the block is left or right
        '''
        if grid[y][x + direc[0]] == 'o' or grid[y][x + direc[0]] == 'x':
            new_dir = direc
        elif grid[y][x + direc[0]] == 'a':
            new_dir = [-1 * direc[0], direc[1]]
        elif grid[y][x + direc[0]] == 'b':
            new_dir = []
        elif grid[y][x + direc[0]] == 'c':
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
    MAX_ITER = 100
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


if __name__ == "__main__":
    # Trial for Grid 1 -  for 1 lazor 1 hole 1 type of block
    '''
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
    origin = (3,0)
    direc = (1, 1)
    hole = [[2,1]]
    '''
    # Trial for Grid 2 - for a bigger matrix with the same paramters as above
    '''
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append('x')
    grid[1][1] = 'o'
    grid[1][3] = 'o'
    grid[1][5] = 'a'
    grid[3][1] = 'o'
    grid[3][5] = 'o'
    grid[3][7] = 'a'
    grid[5][1] = 'a'
    grid[5][5] = 'o'
    grid[7][3] = 'o'
    grid[7][5] = 'o'
    for i in range(len(grid)):
        print(grid[i])
    origin = (1, 8)
    direc = (1, -1)
    hole = [[4, 7]]
    '''
    # Trial for Grid 3 - for 1 lazor same type of blocks but multiple holes
    '''
    grid = []
    for i in range(7):
        grid.append([])
        for j in range(9):
            grid[i].append('x')
    for i in range(3):
        for j in range(4):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][3] = 'a'
    grid[3][1] = 'a'
    grid[5][3] = 'a'
    grid[5][5] = 'a'
    origin = (7,0)
    direc = (-1, 1)
    hole = [[2, 3], [4, 3], [6, 3]]
    '''
    # Trial for Grid 4 - for 1 lazor and 1 hole and absorbing block
    '''
    grid = []
    for i in range(7):
        grid.append([])
        for j in range(7):
            grid[i].append('x')
    grid[1][5] = 'b'
    grid[3][1] = 'o'
    grid[3][3] = 'o'
    grid[5][1] = 'b'
    grid[5][3] = 'o'
    origin = (1, 0)
    direc = (1, 1)
    hole = [[6, 5]]
    '''
    # Trial of Grid 5 with 1 lazor, multiple holes and 2 types of blocks 'Mad 1'
    '''
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append('x')
    for i in range(4):
        for j in range(4):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][5] = 'c'
    grid[3][7] = 'a'
    grid[5][1] = 'a'
    origin = (2, 7)
    direc = (1, -1)
    hole = [[3, 0], [4, 3], [2, 5], [4, 7]]
    '''
    # Trial for Grid 6 with 2 lazors, multiple holes and 1 type of reflective blocks 'Braid 4'
    '''
    grid = []
    for i in range(11):
        grid.append([])
        for j in range(9):
            grid[i].append('x')
    for i in range(5):
        for j in range(4):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][5] = 'x'
    grid[7][5] = 'x'
    grid[3][3] = 'a'
    grid[3][7] = 'a'
    grid[7][3] = 'a'
    grid[7][7] = 'a'
    origin1 = (1, 4)
    direc1 = (1, 1)
    origin2 = (1, 6)
    direc2 = (1, -1)
    hole = [[3, 0], [4, 5], [3, 10]]
    '''
    # Trial for Grid 7 with multiple Lazors, mutiple holes, 2 types of Blocks (A and B) 'Numbered 6'
    '''
    grid = []
    for i in range(11):
        grid.append([])
        for j in range(7):
            grid[i].append('x')
    for i in range(5):
        for j in range(3):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[3][3] = 'x'
    grid[3][5] = 'x'
    grid[7][3] = 'x'
    grid[1][1] = 'b'
    grid[3][1] = 'a'
    grid[5][1] = 'b'
    grid[7][1] = 'a'
    grid[9][1] = 'b'
    grid[5][5] = 'a'
    origin1 = (4, 9)
    direc1 = (-1, -1)
    origin2 = (6, 9)
    direc2 = (-1, -1)
    hole = [[5,0], [2,5]]
    '''
    # Trial for Grid 8 with single Lazor, mutiple holes, 2 types of Blocks (A and B) 'Yarn 5'
    '''

    grid = []
    for i in range(13):
        grid.append([])
        for j in range(11):
            grid[i].append('x')
    for i in range(6):
        for j in range(5):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][3] = 'b'
    grid[1][5] = 'x'
    grid[3][3] = 'a'
    grid[5][1] = 'a'
    grid[5][9] = 'a'
    grid[7][5] = 'a'
    grid[9][1] = 'a'
    grid[9][9] = 'a'
    grid[11][1] = 'b'
    grid[11][3] = 'a'
    grid[11][7] = 'a'
    grid[5][3] = 'x'
    grid[7][3] = 'x'
    grid[7][9] = 'x'
    grid[9][5] = 'x'
    grid[9][7] = 'x'
    grid[11][5] = 'x'
    origin1 = (4, 1)
    direc1 = (1, 1)
    hole = [[9,2], [6,9]]
    '''
    # Trial for Grid 9 with single Lazor, mutiple holes, 3 types of Blocks (A and B and C) 'Yarn 5'
    '''

    grid = []
    for i in range(7):
        grid.append([])
        for j in range(7):
            grid[i].append('x')
    for i in range(3):
        for j in range(3):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][1] = 'a'
    grid[1][3] = 'b'
    grid[3][5] = 'a'
    grid[5][1] = 'a'
    grid[5][3] = 'c'
    origin1 = (4, 5)
    direc1 = (1, -1)
    hole = [[6,3], [1,2]]
    '''
    # Trial for Grid 10 with single Lazor, one hole, 2 types of Blocks (A and B) 'Showstopper-4'
    '''

    grid = []
    for i in range(7):
        grid.append([])
        for j in range(7):
            grid[i].append('x')
    for i in range(3):
        for j in range(3):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][1] = 'b'
    grid[1][3] = 'a'
    grid[1][5] = 'b'
    grid[3][1] = 'b'
    grid[3][5] = 'a'
    grid[5][1] = 'a'
    grid[5][5] = 'b'
    origin1 = (3, 6)
    direc1 = (-1, -1)
    hole = [[2,3]]
    '''
    # Trial for Grid 11 with 2 Lazors, mutiple holes, 1 type of Blocks (A) 'Mad-7'
    '''

    grid = []
    for i in range(11):
        grid.append([])
        for j in range(11):
            grid[i].append('x')
    for i in range(5):
        for j in range(5):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][5] = 'a'
    grid[3][7] = 'a'
    grid[5][1] = 'a'
    grid[5][5] = 'a'
    grid[7][7] = 'a'
    grid[9][5] = 'a'
    grid[5][9] = 'x'
    origin1 = (2, 1)
    direc1 = (1, 1)
    origin2 = (9,4)
    direc2 = (-1, 1)
    hole = [[6,3], [6,5], [6,7], [9,6], [2,9]]
    '''
    # Trial for Grid 12 with 1 Lazors, mutiple holes, 1 type of Blocks (A) 'Mad-4'
    '''

    grid = []
    for i in range(11):
        grid.append([])
        for j in range(9):
            grid[i].append('x')
    for i in range(5):
        for j in range(4):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[3][3] = 'a'
    grid[5][1] = 'a'
    grid[7][3] = 'a'
    grid[7][7] = 'a'
    grid[7][7] = 'a'
    grid[9][5] = 'a'
    origin1 = (7, 2)
    direc1 = (-1, 1)
    hole = [[7,4], [3,4], [5,8]]
    '''
    # Trial for Grid 13 with 1 Lazors, mutiple holes, 2 type of Blocks (A, C) 'Mad-1'
    '''

    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append('x')
    for i in range(4):
        for j in range(4):
            grid[2 * i + 1][2 * j + 1] = 'o'
    grid[1][5] = 'c'
    grid[3][7] = 'a'
    grid[5][1] = 'a'
    origin1 = (2, 7)
    direc1 = (1, -1)
    hole = [[3,0], [4,3], [4,7], [2,5]]
    '''
   
    if lazor_path(grid, [[origin1, direc1]], hole):
        print("Congo")
    else:
        print("Try again")