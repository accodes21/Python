# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:28:39 2022

@author: HP
"""

n=int(input("ENter n"))
x=len(str(n))
sum=0
temp=n
while temp>0:
    digit = temp%10
    sum += digit**x
    temp //= 10
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")