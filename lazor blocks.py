#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:09:11 2019

@author: charan
"""
import time
from itertools import *
import copy

def read_bff(filename):
    grid = []
    A_blocks = []
    B_blocks = []
    C_blocks = []
    lazor_ori = []
    hole = []
    bff_read = open(filename, "r").read()
    file_content = bff_read.strip().split("\n")
#    print(file_content)

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

#    print(grid, A_blocks, B_blocks, C_blocks, lazor_ori, hole)

    return(grid, A_blocks, B_blocks, C_blocks, lazor_ori, hole)



def blocks(grid, A_blocks, B_blocks, C_blocks):
    #As the grid is returned as something like this ()
    updated_grid = [] 
    for x in grid: 
        lists = x.split(' ') 
        updated_grid.append(lists)
#    print (updated_grid)
    
    
    '''
    This creates an empty list and adds those postions which have 'o's
    '''
    empty_blocks=[]
    for x in updated_grid:
        for y in x :
            if y == 'o':
                empty_blocks.append(y)
                
#    print (empty_blocks)
    
    
    '''
    The returned blocks are in the form of lists, to convert into interger the below code is applied
    '''
    if A_blocks==[]:
        A_blocks=0
    else:
        A_blocks=A_blocks[0]
    
    if B_blocks==[]:
        B_blocks=0
    else:
        B_blocks= B_blocks[0]
        
    if C_blocks==[]:
        C_blocks=0 
    else:
        C_blocks= C_blocks[0] 
          
    
    '''
    adds and replace the 'o's with the blocks in the list from 1st postion
    '''
    
    for i in range(A_blocks):
        empty_blocks[i] = 'A'
    for i in range(A_blocks, (A_blocks+B_blocks)):
        empty_blocks[i] = 'B'
    for i in range((A_blocks+B_blocks), (A_blocks+B_blocks+C_blocks)):
        empty_blocks[i] = 'C'
        
        
#    print (empty_blocks)
    '''
    To find all the possible permutations of the different types of blocks, 
    we used permutations function and set function to remove the repeats
    As it gives a list of tuples, listen_posibilites is to make it a list of lists 
    '''
    posibilities=set(permutations(empty_blocks))
    print (len(posibilities))
    listen_posibilites=[list(t) for t in posibilities]
#    print (listen_posibilites)
    
    '''
    To put back this list in our grid, 
    we check and replace the values of the original grid to the one present in listed_possibilites
    '''
    length=len(updated_grid)
    width=len(updated_grid[0])
    
    for value in listen_posibilites:
#       possible_grid = [['x', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'x']]
        possible_grid = copy.deepcopy(updated_grid)
        counter = 0
        for i in range(length):
            for j in range (width):
                if possible_grid[i][j] == 'o':
                    possible_grid[i][j] = value[counter]
                    counter +=1
        listen_posibilites.remove(value)
                    
        print (possible_grid)
        

                    
                    
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    grid, A_blocks, B_blocks, C_blocks, lazor_ori, hole=read_bff("dark_1.bff")
    blocks(grid, A_blocks, B_blocks, C_blocks)
    time_start = time.time()
    time_end = time.time()
    print('run time: %f seconds' %(time_end - time_start))
