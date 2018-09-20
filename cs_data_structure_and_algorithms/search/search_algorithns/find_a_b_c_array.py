#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))

from  sort.sort_category.heap_sort import HeapSort

class FindABCArray(object):
    def __init__(self, data,array=[]):
        self.data = data
        self.array = array

    def get_a_b_c(self):
        n = len(self.array)
        t= HeapSort()
        A = t.sort(self.array)
        a = []
        for k in range(n):
            i = k+1
            j = n-1

            while i < j:

               if A[k] + A[i] + A[j] == self.data:
                   a.append([A[i],A[j],A[k]])

               elif A[k] + A[i] + A[j] < self.data:
                   i = i + 1
               else:
                   j = j - 1

        return a

if __name__ == "__main__":
    mm = [3, 2, 5, 7, 23, 6, 8, 5, 3, 6, 9, 89, 65, 78, 0, 6, 4, 5, 8, 54, 7, 891, 2, 4, 6, 6, 345]
    t = FindABCArray(12,mm)
    print(t.get_a_b_c())