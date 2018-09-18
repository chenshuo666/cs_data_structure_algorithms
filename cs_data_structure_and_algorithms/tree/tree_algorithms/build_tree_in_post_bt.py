#!/usr/bin/python
# -*- coding:utf-8 -*-
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


class BuildTreeInpost():
    def __init__(self, post_order, in_order):
        self.post_order = post_order
        self.in_order = in_order

    def build_tree(self, post_order, in_order):
        if len(post_order) == 0:
            return None
        root_data = post_order[-1]
        i = in_order.index(root_data)
        left = self.build_tree(post_order[ : i], in_order[ : i])
        right = self.build_tree(post_order[ i : -1], in_order[i + 1:])
        return Node(root_data, left, right)


if __name__ == '__main__':
    t = BinaryTree()
    post_order = [7, 4, 2, 5, 8, 6, 3, 1]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    m = BuildTreeInpost(post_order, in_order)
    root = m.build_tree(post_order, in_order)
    t.root = root
    print(t.hierarchicalorder())
    print(t.preorder(t.root))