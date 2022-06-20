#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 12:40:01 2022

@author: kunyang
"""

s = "PAYPALISHIRING"
numRows = 3

n = 2*numRows - 2
rows = [""]*numRows #创建一个n维矩阵

for i, char in enumerate(s):  #i是字符串索引值，char是字符串索引所代表的值
#enumerate是将字符串的索引与值一一对应的打印出来
    print(i,char)
    x = i%n
    rows[min(x,n-x)] += char #将对应的值放到新建的列表rows中!!
print("".join(rows))
