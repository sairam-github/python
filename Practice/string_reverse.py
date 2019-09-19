# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:10:56 2019

@author: smadem
"""

s = 'time'
#original string and reverse a string
print(s[::])
print(s[::-1]) #method-1

#method-2
length = len(s)
print(s[length::-1])

#method-3
print(reversed(s))