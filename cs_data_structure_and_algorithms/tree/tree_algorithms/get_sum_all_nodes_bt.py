#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetSumAllNodes():
    def __init__(self,tree):
        self.tree = tree

    def get_sum_recursive(self, root):
        if root is None:
            return 0
        else:
            return root.data+self.get_sum_recursive(root.left)+self.get_sum_recursive(root.right)

    def get_sum_nonrecursive(self):
        if self.tree.root is None:
            return None
        else:
            res = self.tree.root.data
            node_array = [self.tree.root]
            while node_array != []:
                pop_node = node_array.pop(0)
                if pop_node.left is not None:
                    node_array.append(pop_node.left)
                    res += pop_node.left.data

                if pop_node.right is not None:
                    node_array.append(pop_node.right)
                    res += pop_node.right.data
        return res

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetSumAllNodes(t)
    print(m.get_sum_recursive(t.root))
    print(m.get_sum_nonrecursive())