#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:59:19 2022

@author: kunyang
"""
x = " word and 716"
res = []
for i in x:
    
    if i == '-':
        res.append(i)
    
    elif i.isnumeric() is True and i != '0':
        res.append(i)
        

    elif res != [] and i.isnumeric() is False:
        break
    
n = ''.join(res)

max, min = 2**31, 2**31

min = -max

if int(n) >=  min-1 and int(n) <= max:
    print(int(n))
elif int(n) < min-1:
    print(min-1)
elif int(n) > max:
    print(max)