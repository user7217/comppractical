# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:37:01 2023

@author: Administrator
"""

#Q14 
strn = str(input("enter stringu "))
lis = strn.split(" ")
for i in range(0, len(lis)):
    x = len(lis[i]) -1 
    w = lis[i]
    if w[x] == 't' or w[x] == 'd':
        print(lis[i])