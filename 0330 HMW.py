# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:17:23 2022

@author: user
"""

z = [[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]

for i in range (5):
    for x in range(i+1):
        print(z[i][x],sep="",end="")
    print()