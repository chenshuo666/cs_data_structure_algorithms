#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from tree_category.binary_tree import BinaryTree

class GetDiameter(object):
    def __init__(self,tree):
        self.tree = tree

    def diameter(self, root):
        self.diameter = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right +1)
            return max(left, right) + 1
        dfs(root)
        return self.diameter

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetDiameter(t)
    print(m.diameter(t.root))
