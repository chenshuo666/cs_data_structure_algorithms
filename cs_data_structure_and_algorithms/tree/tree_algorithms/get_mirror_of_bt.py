#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetMirror():
    def __init__(self,tree):
        self.tree = tree

    def get_mirror_recursive(self, root):
        if root is None:
            return 0
        else:
            self.get_mirror_recursive(root.left)
            self.get_mirror_recursive(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp

        return root

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetMirror(t)
    m.get_mirror_recursive(t.root)