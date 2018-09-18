#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
class BuildTreeInPre():
    def __init__(self,pre_order,in_order):
        self.pre_order = pre_order
        self.in_order  = in_order

    def build_tree(self,preorder, midorder):
        if len(preorder) == 0:
            return None
        root_data = preorder[0]
        i = midorder.index(root_data)
        left = self.build_tree(preorder[1: 1 + i], midorder[:i])
        right = self.build_tree(preorder[1 + i:], midorder[i + 1:])
        return Node(root_data, left, right)

if __name__ == '__main__':
    t= BinaryTree()
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    midorder = [4, 7, 2, 1, 5, 3, 8, 6]
    m = BuildTreeInPre(preorder,midorder)
    root = m.build_tree(preorder, midorder)
    t.root = root
    print(t.hierarchicalorder())
    print(t.preorder(t.root))
    print(t.postorder(t.root))