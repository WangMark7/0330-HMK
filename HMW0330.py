# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:18:36 2022

@author: user
"""

def jin():
    data = []
    while len (data) < 3 :
        x = int(input("請輸入: "))
        data.append(x)
        data.sort()
    print(data)