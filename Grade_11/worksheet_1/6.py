# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:10:05 2023

@author: Administrator
"""

strn = str(input("enter a string: "))
for i in strn:
    if i == 'a':
        
        s = strn.replace(i, '$')
print(s)
