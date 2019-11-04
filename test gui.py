#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:19:37 2019

@author: charan
"""
from PIL import Image, ImageDraw

# DEFINE THINGS
x = 0
o = 1
A = 2
B = 3
C = 4

COLORS = {
    'x': (20, 20, 20),
    'A': (255, 255, 255),
    'B': (0, 0, 0),
    'C': (192, 192, 192),
    'o': (50, 50, 50),
}



def set_color(img, x0, y0, dim, color):
    for x in range(dim):
        for y in range(dim):
            
            img.putpixel(
                (dim * x0 + x, dim * y0 + y),
                color)
            draw = ImageDraw.Draw(img)
            draw.rectangle([(x, y),(x+6,y+6)], fill=255)


def save_maze(maze, blockSize=20, basename="maze"):

    w_blocks = len(maze[0])
    h_blocks = len(maze)
    print (w_blocks,h_blocks)
    SIZE = (w_blocks * blockSize, h_blocks * blockSize)
    img = Image.new("RGB", SIZE, color=COLORS['x'])

    for y, row in enumerate(maze):
        for x, block_ID in enumerate(row):
            set_color(img, x, y, blockSize, COLORS[block_ID])

    img.save("%s_%d_%d_%d.png"
             % (basename, w_blocks, h_blocks, blockSize))
    
    
    
if __name__ == "__main__":
 test_maze = [['x', 'x', 'x', 'x', 'x', 'x', 'x'],
              ['x', 'x', 'x', 'o', 'x', 'o', 'x'],
              ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
              ['x', 'o', 'x', 'B', 'x', 'o', 'x'],
              ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
              ['x', 'B', 'x', 'B', 'x', 'x', 'x'],
              ['x', 'x', 'x', 'x', 'x', 'x', 'x']]
 save_maze(test_maze, blockSize=20)   
    
