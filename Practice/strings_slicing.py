# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:30:57 2019

@author: smadem
"""

s = "The trouble is you think you have time"
#print(s)

#print(s[:6]) #starts at 0th index until 5th index (excluding mentioned index)

#print(s[4:]) #starts at 4th index until end

#print(s[:])  #prints same string

#original string and reverse a string
print(s[::])
print(s[::-1]) #method-1

#method-2
length = len(s)
print(s[length::-1])