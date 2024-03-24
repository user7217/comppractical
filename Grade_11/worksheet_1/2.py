# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:52:37 2023

@author: Administrator
"""

strn = str(input("enter string"))
print(sum(map(lambda x: 1 if 'o' in x else 0,strn)))