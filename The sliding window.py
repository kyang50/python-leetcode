#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:56:14 2022

@author: kunyang
"""

s = "abcabcbb"

dic = {}
res = 0
i =  0   #i是左指针
for j in range(len(s)):  #j是右指针
    if s[j] in dic:     #若当前元素在之前出现过，更新左指针
   #当之前出现的元素在左右指针中间，左指针更新为之前元素下标，若不在中间，左指针不变
       i = max(i, dic[s[j]])#例如第二次出现元素a，dic[s[j]]=0,所以左指针位置不变，i=0
                            #第二次出现b的时候，dic[s[j]]=1,左指针变为1
                            #第二次出现c的时候，dic[s[j]]=2,左指针变为2
                            #第三次出现b的时候，dic[s[j]]=4,左指针变为4
       
       
    dic[s[j]] = j    #如果这个元素不在哈希表内，将当前元素加入哈希表中
    res = max(res, j - i) #这一步实现对比大小，每一次都进行对比，将大的留下！
    print(i,j)
    #print(res)
print(res)

