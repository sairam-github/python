# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:47:08 2019

@author: smadem
"""

def outer():
    #test = 1
    
    def inner():
        #test = 2
        print('inner:', test)
    inner()
    print('outer', test)
test = 0
outer()
print('global', test)
    