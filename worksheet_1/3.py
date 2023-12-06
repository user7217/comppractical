# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:57:41 2023

@author: Administrator
"""

strn = str(input("enter a string: "))
count_c = 0
for i in strn:
    if i.isalpha():
        if i not in('a', 'e', 'i', 'o', 'u'):
            count_c+=1
print(count_c)