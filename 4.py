# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:02:27 2023

@author: Administrator
"""

strn = str(input("enter a string: "))
count_v = 0
for i in strn:
    if i.isalpha():
        if i in('a', 'e', 'i', 'o', 'u'):
            count_v+=1
print(count_v)