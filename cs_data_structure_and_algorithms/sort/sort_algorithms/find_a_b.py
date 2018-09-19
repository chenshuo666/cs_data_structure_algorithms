#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))

from sort_category.heap_sort import HeapSort
from tree.tree_category.binary_tree import BinaryTree

class FindAB(object):
    def __init__(self, data, array=[], array1 = []):

        self.array = array
        self.array1 = array1
        self.k = data

    def get_a_b(self):
        if len(self.array) != len(self.array1):
            return False
        else:
            t= HeapSort()
            A = t.sort(self.array)
            for i in range(len(self.array)):
                c = self.k  -  self.array1[i]
                tree = BinaryTree()
                for i in A:
                    tree.add(i)
                if tree.get_data_by_self(tree.root,c):
                    return True

        return False

if __name__ == "__main__":
    mm = [3, 2, 5, 7, 23, 6, 8, 5, 3, 6, 9, 89, 65, 78, 0, 6, 4, 5, 8, 54, 7, 891, 2, 4, 6, 6, 345]
    mm1 = [3, 2, 5, 7, 23, 6, 8, 5, 3, 6, 9, 89, 65, 78, 0, 6, 4, 5, 8, 54, 7, 891, 2, 4, 6, 6, 345]
    t = FindAB(5,mm,mm1)
    print(t.get_a_b())