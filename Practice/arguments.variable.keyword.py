# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:00:22 2019

@author: smadem
"""

def func(**kwargs):
    print(kwargs)

func(a=1, b=2)
func(**{'a': 1, 'b': 2})
func(**dict(a=1, b=2))