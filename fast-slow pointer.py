#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 00:43:21 2022

@author: kunyang
"""
s = [1,1,2,2,3]

#1)s[slow]=1;s[fast]=1,相等，fast += 1;
#2)s[slow]=1;s[fast]=2,不相等,slow += 1, s[slow]= s[fast], 
#也就是s[1]=s[2];s=[1,2,2,2,3],此时s[slow]=2
#3)s[slow]=2;s[fast]=2,相等,fast+=1
#4)s[slow]=2;s[fast]=3,不相等,slow+=1,s[slow]=s[fast]
#s[2]=s[4],s=[1,2,3,2,3],此时fast=len(s),结束循环,打印内容为print(s[:slow+1])

slow = 0
fast = 1
while fast < len(s):
    if s[slow] != s[fast]:
        slow += 1
        s[slow] = s[fast]
        print(slow)
    fast += 1
print(s[:slow+1])