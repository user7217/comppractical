# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:46:18 2023

@author: Administrator
"""
#this is another comment
strn = str(input("enter stringu "))
lis = strn.split(" ")
for i in range(0, len(lis)):
    if lis[i][0] in ('a', 'e', 'i', 'o', 'u'):
        print(lis[i])