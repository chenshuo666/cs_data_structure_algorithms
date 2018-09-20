#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from sort.sort_category.quick_sort import QuickSort

def FindFirstNumber(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                return array[i]


print(FindFirstNumber([1,2,3,4,5,6,7,8,93,4,5,63,3,4,5,64,4,4,4]))