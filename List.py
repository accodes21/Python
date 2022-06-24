# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:41:34 2022

@author: HP
"""

a = [1,2,3,4,5,6,7]

print(len(a))

print(a[0])

b = [8,9,10]

print(a+b)

c = 11
a.append(c)
print(a)

print(a[-5:-1])

d = [1,2,3,2,4]
d.remove(2)
print(d)

print(a[::-1])

e = [5,3,6,2,1]
e.sort()
print(e)