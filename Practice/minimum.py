# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:16:46 2019

@author: smadem
"""

def FindMin(*input):
    print(input)
    if input:
        mn = input[0]
        for value in input[1:]:
            if value < mn:
                mn = value
        return mn

print(FindMin(1, 0))