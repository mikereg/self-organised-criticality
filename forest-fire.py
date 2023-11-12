#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:51:15 2023

@author: michaelreginiano
"""
import numpy as np

#generating initial random forest
grid = np.random.randint(0,2,(5,5))


def moore_neighbourhood(x,y,grid):
    x_lower,x_upper = 1,1
    y_lower,y_upper = 1,1
    GRID_LENGTH = grid.shape[0]
    
    if (x==0) & (y==0):
        x_lower,y_lower=0,0
    elif x==0:
        x_lower=0
    elif y==0:
        y_lower=0
    
    if (x==GRID_LENGTH) & (y==GRID_LENGTH):
        x_upper,y_upper=0,0
    elif x==GRID_LENGTH:
        x_upper=0
    elif y==GRID_LENGTH:
        y_upper=0
    
    row_start = x-x_lower
    row_end = x+x_upper+1
    
    col_start = y-y_lower
    col_end = y+y_upper+1
    
    
    return grid[row_start:row_end,col_start:col_end]

print(grid)
print('====== Trees ======')
x,y = np.where(grid == 1)[0], np.where(grid == 1)[1]
trees = np.array([(x[i],y[i]) for i in range(0,len(x))], dtype=tuple)
print(trees)
print('====== Moore Neighbourhood ======')
print(moore_neighbourhood(trees[1][0],trees[1][1],grid))


