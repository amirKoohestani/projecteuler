# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:41:53 2023

@author: Amir
"""

number = 600851475143 
largePrime = [2]
prime = True

for i in range(3, int(number/2)):
    if number % i == 0:
        for j in largePrime:
            if i % j == 0:
                prime = False
                break
        if prime:
            largePrime.append(i)
            
        
print(largePrime)