# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:33:42 2019

@author: smadem
"""

def func(*args):
    print(args)

values = (1, 3, -7, 9)
func(values)
func(*values)