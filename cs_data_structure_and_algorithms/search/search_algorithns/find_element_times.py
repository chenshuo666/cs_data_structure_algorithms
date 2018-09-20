#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))

from  sort.sort_category.quick_sort import QuickSort

class BubbleSort(object):
    def __init__(self,array = []):
        self.array = array

    def sort(self):
        t = QuickSort()
        A = t.sort(self.array,0,len(self.array)-1)
        a = {}
        i = 0
        while i < len(A):
            j = i
            count = 0
            flag = True
            while j < len(A) and flag == True:
                if A[i] == A[j]:
                    count += 1
                    j += 1
                    if j == len(A):
                        a[A[i]] = count
                        i = j
                else:
                    a[A[i]] = count
                    i = j
                    flag = False
        return a


if __name__=="__main__":
    mm = [1,1,2,3,1,2,3,4,5,6,1,2,4,5,7,8,4,6,7,56,5,4,34,3,2]
    t=BubbleSort(mm)
    print(t.sort())