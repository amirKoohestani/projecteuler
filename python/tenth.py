# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:05:47 2023

@author: Amir
"""

primes = [2]
sum = 2

for i in range(3, 2000001):
    isPrime = True
    for j in primes:
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
        sum += i
    
print(sum)