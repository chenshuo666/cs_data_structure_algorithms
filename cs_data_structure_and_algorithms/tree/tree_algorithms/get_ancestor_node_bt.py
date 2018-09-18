#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from tree_category.binary_tree import BinaryTree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class GetAncestor(object):
    def __init__(self,tree):
        self.tree = tree

    def find(self,root,node):
        res = []
        if root == None:
            return
        if root.data == node.data:
            return True

        if root.left == node or root.right == node or self.find(root.left,node) or self.find(root.right,node):
            print(root.data)
            return 1
        return 0

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)
    node = Node(9)
    m = GetAncestor(t)
    m.find(t.root,node)



