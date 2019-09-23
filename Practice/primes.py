# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:28:56 2019

@author: smadem
"""

primes = []
max = 100

for n in range(2, max + 1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
        
    if is_prime:
        primes.append(n)

print(primes)