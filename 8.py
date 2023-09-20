# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:13:43 2023

@author: Administrator
"""

strn = str(input("enter a string: "))
upper_count = 0
lower_count = 0
for i in strn:
    if i.isalpha():
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
print('upper count: ',upper_count, "lower count", lower_count)