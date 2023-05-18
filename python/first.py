# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:40:17 2023

@author: Amir
"""

sum = 0

for i in range(1,1000):
    if i % 5 == 0 or i % 3 == 0:
        sum += i
    
print(sum)