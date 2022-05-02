#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 02:26:49 2022

@author: kunyang
"""

x = "    I love FishC.     "
#x = x.strip()


y = x.split(' ') #将字符串分割，以空格为分界线
print(y)
raw = []

for i in y: #找到单词，排除空格
    if i != '':
        print("yes")
        raw.append(i)
    else:
        continue

print(raw)

z = list(reversed(raw)) #反转

print(' '.join(z)) #加入空格
