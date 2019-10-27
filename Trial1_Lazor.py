'''
This is to try the algo
to solve the lazor problem
'''
import random


def solve(grid, start_pt, next_pt, end_pt):
    '''
    Grid is the n*n matrix
    start_pt = array - origin of the lazor
    next_pt = array - to find the initial slope of the lazor
    end_pt = array - sink/hole
    '''
    m = (next_pt[1] - start_pt[1]) / (next_pt[0] - start_pt[0])
    c = next_pt[1] - m * next_pt[0]
    sign = next_pt[0] - start_pt[0] / abs(next_pt[0] - start_pt[0])
    n = len(grid)
    stack = []
    stack[-1] = start_pt
    while len(stack) != 0:
        incid_pts = []
        curr_pt = stack[-1]
        if sign > 0:
            start_x = curr_pt[0]
            end_x = n
            start_y = curr_pt[1]
            end_y = n
        else:
            start_x = 0
            end_x = curr_pt[0]
            start_y = 0
            end_y = curr_pt[1]
        for i in range(start_x, end_x):
            x = i
            for j in range(start_y, end_y):
                y = j
                if y == (m * x + c):
                    incid_pts.append([x, y])
        m = (-1 / m)
        n_1 = len(incid_pts)
        poss_pos = []
        for i in range(n_1):
            next_pos = incid_pts[i]
            c = next_pos[1] - (m * next_pos[0])
            poss_pos_nxt = []
            if next_pos[1] > next_pos[0] and m < 0:
                start_x = 0
                end_x = next_pos[0]
                start_y = 0
                end_x = next_pos[1]
            elif next_pos[1] > next_pos[0] and m > 0:
                start_x = 0
                end_x = next_pos[0]
                start_y = next_pos[1]
                end_x = n
            elif next_pos[1] < next_pos[0] and m > 0:
                start_x = next_pos[0]
                end_x = n
                start_y = 0
                end_x = next_pos[1]
            elif next_pos[1] < next_pos[0] and m < 0:
                start_x = next_pt[0]
                end_x = n
                start_y = next_pt[1]
                end_y = n
            else:
                print("Solution not possible")
            for i in range(start_x, end_x):
                x = i
                for j in range(start_y, end_y):
                    y = j
                    if y == (m * x + c):
                        poss_pos_nxt.append([x, y])
            if len(poss_pos_nxt) > 1:
                poss_pos.append(next_pt)
        if len(poss_pos) > 1:
            next_pos = random.choice(incid_pts)
            stack.append[next_pos]
        else:
            stack.pop()





if __name__ == "__main__":
    pass
