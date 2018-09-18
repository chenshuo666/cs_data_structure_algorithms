#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class JudgeMirror():
    def __init__(self,tree,tree1):
        self.tree = tree
        self.tree1 = tree1

    def judge(self,root,root1):
        if root == None and root1 == None:
            return True
        if root == None or root1 == None:
            return False
        if root.data != root1.data:
            return False
        else:
            return self.judge(root.left,root.right) and self.judge(root.right,root.left)

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)
    t2 = BinaryTree()
    for i in range(10):
        t2.add(i)

    m = JudgeMirror(t,t2)

    print(m.judge(t.root,t2.root))