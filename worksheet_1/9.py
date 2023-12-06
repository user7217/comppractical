# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:15:45 2023

@author: Administrator
"""

strn = str(input("enter a string: "))
num_count = 0
special_count = 0
for i in strn:
    if i.isdigit():
        num_count = 0
    elif i.isalpha():
        continue
    elif i.isspace():
        continue
    else:
        special_count +=1
print(num_count, special_count)