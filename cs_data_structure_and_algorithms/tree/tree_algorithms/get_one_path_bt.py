#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetOnePath():
    def __init__(self,tree,input):
        self.tree = tree
        self.input = input

    def get_one_path(self, root):
        # Write your code here
        path = ''
        res = []
        self.paths(root, path, res)
        return res

    def paths(self, root, path, res):
        if root is None:
            return
        self.input -= root.data
        path += str(root.data)
        if root.left is not None:
            self.paths(root.left, path + '->', res)
        if root.right is not None:
            self.paths(root.right, path + '->', res)
        if root.left is None and root.right is None:
            if self.input == 0:
                res.append(path)

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetOnePath(t,11)
    print(m.get_one_path(t.root))