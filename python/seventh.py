# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:55:16 2023

@author: Amir
"""

prime = [2]
counter = 3

while len(prime) < 10001:
    isPrime = True
    for i in prime:
        if counter % i == 0:
            isPrime = False
            break
    if isPrime:
        prime.append(counter)
    counter += 1
        
print(prime[10000])


i=3
k=1 
while i<100000000:
    j=2
    while i > j:
        if i % j == 0:
            break
        if i == j+1:
            k += 1
            break
        j += 1
    if k == 10001:
        print("solved prime  ", i," is the ",k,"st prime number.")
        break
    i += 1