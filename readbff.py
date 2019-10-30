# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:48:06 2019

@author: Wayne Monteiro
"""


def read_bff(filename):
    grid = []
    A_blocks = []
    B_blocks = []
    C_blocks = []
    lazor_ori = []
    hole = []
    bff_read = open(filename, "r").read()
    file_content = bff_read.strip().split("\n")
    print(file_content)

    for i in range(len(file_content)):
        if file_content[i] == "GRID START":
            a = i+1
            while file_content[a] != "GRID STOP":
                grid.append(file_content[a])
                a = a + 1
        if len(file_content[i]) == 3 and file_content[i][0] == "A":
            A_blocks.append(int(file_content[i][2]))
        if len(file_content[i]) == 3 and file_content[i][0] == "B":
            B_blocks.append(int(file_content[i][2]))
        if len(file_content[i]) == 3 and file_content[i][0] == "C":
            C_blocks.append(int(file_content[i][2]))

        if len(file_content[i]) != 0 and file_content[i][0] == "L":
            strip_lazor = file_content[i].split(" ")
            for j in range(1, len(strip_lazor), 2):
                lazor_ori.append((int(strip_lazor[j]), int(strip_lazor[j+1])))

        if len(file_content[i]) != 0 and file_content[i][0] == "P":
            hole.append((int(file_content[i][2]), int(file_content[i][4])))

    print(grid, A_blocks, B_blocks, C_blocks, lazor_ori, hole)

    return(grid, A_blocks, B_blocks, C_blocks, lazor_ori, hole)


if __name__ == "__main__":
    read_bff("yarn_5.bff")
