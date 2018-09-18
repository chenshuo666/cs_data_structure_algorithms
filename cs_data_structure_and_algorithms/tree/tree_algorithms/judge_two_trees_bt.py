#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from tree_category.binary_tree import BinaryTree

class JudgeTwoTrees(object):
    def __init__(self,tree,tree1):
        self.tree = tree
        self.tree1 = tree1

    def judge(self,root,root1):
        if root == None and root1 == None:
            return True
        if root == None or root1 == None:
            return False
        return (root.data == root.data and self.judge(root.left,root1.left) and  self.judge(root.right,root1.right))

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    t1 = BinaryTree()
    for i in range(10):
        t1.add(i)

    m = JudgeTwoTrees(t,t1)
    print(m.judge(t.root,t1.root))


