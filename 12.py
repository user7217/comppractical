# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:33:02 2023

@author: Administrator
"""

strn = str(input("enter stringu "))
lis = strn.split(" ")
for i in range(0, len(lis)):
    if len(lis[i]) == 5:
        print(lis[i])
    else:
        pass 
    