#!/usr/bin/python
# -*- coding:utf-8 -*-
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
    def __init__(self, tree):
        self.tree = tree

    def find(self, root, node, node1):
        if (root is None or root == node or root == node1):
            return root
        left = self.find(root.left, node, node1)
        right = self.find(root.right, node, node1)
        if (left is not None and right is not None):
            return root
        if (left is None):
            return right
        if (right is None):
            return left


if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)
    node = Node(9)
    node1 = Node(8)
    m = GetAncestor(t)
    print(m.find(t.root, node, node1))
