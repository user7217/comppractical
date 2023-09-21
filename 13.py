# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:35:35 2023

@author: Administrator
"""

#Q13

strn = str(input("enter stringu "))
lis = strn.split(" ")

for i in range(0, len(lis)):
    if lis[i][0] == 'a' or lis[i] == 'A':
        print(lis[i][0])
    else:
        pass
    