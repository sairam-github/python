# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:55:30 2019

@author: smadem
"""

income = 50000
if income < 10000:
    tax_coeff = 0.0
elif income < 30000:
    tax_coeff = 0.2
else:
    tax_coeff = 0.5


print('I will pay', income * tax_coeff, 'in taxes')