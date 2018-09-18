#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetAllPath():
    def __init__(self,tree):
        self.tree = tree

    def get_all_paths(self, root):
        # Write your code here
        path = ''
        res = []
        self.paths(root, path, res)
        return res

    def paths(self, root, path, res):
        if root is None:
            return
        path += str(root.data)
        if root.left is not None:
            self.paths(root.left, path + '->', res)
        if root.right is not None:
            self.paths(root.right, path + '->', res)
        if root.left is None and root.right is None:
            res.append(path)

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetAllPath(t)
    print(m.get_all_paths(t.root))