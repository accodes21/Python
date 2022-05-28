# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:08:05 2022

@author: HP
"""

for x in range(0,6):
    for y in range(0,x+1):
        print("* ", end="")
    print("\r")
    
for x in range(6,0,-1):
    for y in range(0,x):
        print("* ", end="")
    print("\r")