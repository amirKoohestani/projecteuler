# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:18:04 2023

@author: Amir
"""

for i in range(2520, 1000000000):
    found = True
    for j in range(1, 21):
        if i % j != 0:
            found = False
            break
    if found:
        print(i)
        break


"""    
def smallest_divisor(a, b):
    if b == 0:
        return a
    return smallest_divisor(b, a % b)

def smallest_multiple():
    j = 1
    for i in range(1, 21):
        j = (j*i) / smallest_divisor(j,i)
    return int(j)

print(smallest_multiple())
"""