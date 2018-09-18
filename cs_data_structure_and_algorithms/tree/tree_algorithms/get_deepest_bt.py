#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from tree_category.binary_tree import BinaryTree

class GetDeepest(object):
    def __init__(self,tree):
        self.tree = tree

    def get_deepest(self):
        if self.tree.root is None:
            return None
        else:
            node_array=[self.tree.root]
            val=[]
            while node_array:
                val.append([x for x in node_array])
                pop_node=[]
                for i in node_array:
                    if i.left:
                        pop_node.append(i.left)
                    if i.right:
                        pop_node.append(i.right)
                node_array = pop_node
            return val[-1][-1]

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetDeepest(t)
    print(m.get_deepest())
