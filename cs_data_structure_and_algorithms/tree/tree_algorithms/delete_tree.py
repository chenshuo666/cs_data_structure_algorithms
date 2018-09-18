#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

class DeleteTree():
    def __init__(self, tree):
        self.tree = tree

    def delete_recursive(self,root):
        if root == None:
            return -1
        self.delete_recursive(root.left)
        self.delete_recursive(root.right)
        root = None

    def delete_nonrecursive(self, instance):
        """Empty the tree"""
        self.tree.root = None
        self.tree.node_number = 0