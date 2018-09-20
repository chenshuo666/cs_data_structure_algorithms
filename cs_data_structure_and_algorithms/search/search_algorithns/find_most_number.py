#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

def FindMostnNumber(array):
    max = 0
    for i in range(len(array)):
        count = 0
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                count += 1

            if count > max:
                max = count

    return max

print(FindMostnNumber([1,2,3,4,5,6,7,8,93,4,5,63,3,4,5,64,4,4,4]))