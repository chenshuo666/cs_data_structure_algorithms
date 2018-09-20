#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from sort.sort_category.quick_sort import QuickSort

def FindFirstNumber(array):
    t = QuickSort()
    array1 = t.sort(array,0,len(array)-1)
    a = []
    for i in range(1,max(array1)):
        found = 0
        for j in range(0,len(array1)):
            if array1[j] == i:
                found = 1

        if found == 0:
            a.append(i)
    return a


print(FindFirstNumber([1,2,3,4,5,6,7,8,93,4,5,63,3,4,5,64,4,4,4]))