# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:03:27 2023

@author: Amir
"""

sumOfSquare = 0

for i in range(1, 101):
    sumOfSquare += pow(i, 2)
    
sumOfNumbers = 0

for i in range(1, 101):
    sumOfNumbers += i
    
print(pow(sumOfNumbers, 2) - sumOfSquare)