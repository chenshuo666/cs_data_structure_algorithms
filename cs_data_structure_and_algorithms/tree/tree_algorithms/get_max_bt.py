#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetMax(object):
    def __init__(self,tree):
        self.tree = tree

    def get_max_recursive(self,root):
        if root is None:
            return []
        result = [root.data]
        left_data = self.get_max_recursive(root.left)
        right_data = self.get_max_recursive(root.right)
        return max(result ,left_data ,right_data)

    def get_max_nonrecursive(self,root):
        """Hierarchical traversal"""
        if root is None:
            return None
        else:
            self.node_number = 1
            node_array = [root]
            res = root.data
            while node_array != []:
                pop_node = node_array.pop(0)
                if pop_node.left is not None:
                    node_array.append(pop_node.left)
                    if pop_node.left.data > res:
                        res=pop_node.left.data
                    self.node_number  +=1

                if pop_node.right is not None:
                    node_array.append(pop_node.right)
                    if pop_node.right.data > res:
                        res=pop_node.right.data
                    self.node_number += 1
        return res

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(100):
        t.add(i)
    m= GetMax(t)
    print(m.get_max_recursive(t.root)[0])
    print(m.get_max_nonrecursive(t.root))
