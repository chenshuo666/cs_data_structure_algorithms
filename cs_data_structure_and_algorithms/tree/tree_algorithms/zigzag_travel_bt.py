#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from tree_category.binary_tree import BinaryTree


class ZigZag(object):
    def __init__(self, tree):
        self.tree = tree

    def zigzag_travel(self):
        if self.tree.root is None:
            return None
        else:
            node_array = [self.tree.root]
            val = []
            j = 0
            while node_array:
                if j % 2 == 0:
                    val.append([x.data for x in node_array])
                else:
                    val.append([x.data for x in node_array[::-1]])
                pop_node = []
                for i in node_array:
                    if i.left:
                        pop_node.append(i.left)
                    if i.right:
                        pop_node.append(i.right)
                node_array = pop_node
                j += 1

            return val[::]


if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = ZigZag(t)
    print(m.zigzag_travel())
