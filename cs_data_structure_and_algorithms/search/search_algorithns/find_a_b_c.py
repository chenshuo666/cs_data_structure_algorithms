#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))

from  sort.sort_category.heap_sort import HeapSort

class FindABC(object):
    def __init__(self, array=[], array1 = [],array2 = []):

        self.array = array
        self.array1 = array1
        self.array2 = array2

    def get_a_b_c(self):

        t= HeapSort()
        A = t.sort(self.array)
        B = t.sort(self.array1)
        C = t.sort(self.array2)
        a = []
        for i in C:
            for j in B:
               a.append(i-j)

        for n in A:
            if n in a:
                return True
        return False

if __name__ == "__main__":
    mm = [3, 2, 5, 7, 23, 6, 8, 5, 3, 6, 9, 89, 65, 78, 0, 6, 4, 5, 8, 54, 7, 891, 2, 4, 6, 6, 345]
    mm1 = [3, 2, 5, 7, 23, 6, 8, 5, 3, 6, 9, 89, 65, 78, 0, 6, 4, 5, 8, 54, 7, 891, 2, 4, 6, 6, 345]
    mm2 = [3, 2, 5, 7, 23, 6, 8, 5, 3, 6, 9, 89, 65, 78, 0, 6, 4, 5, 8, 54, 7, 891, 2, 4, 6, 6, 345]
    t = FindABC(mm,mm1,mm2)
    print(t.get_a_b_c())