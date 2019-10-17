# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:51:44 2019

@author: smadem
"""

def myFunc1(x1):
    x1 = 10
    print(x1)

def myFunc2(y1):
    y1[0] = 0
    print(y1)
    


x = 5
myFunc1(x)
print(x)

y = [1, 2, 3]
myFunc2(y)
print(y)

z = ''
