#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetData(object):
    def __init__(self,tree):
        self.tree = tree
        
    def get_data_recursive(self,root,data):
        """Determine if there is a node by data"""
        if root == None:
            return False
        else:
            if data == root.data:
                return True
            else:
                bool = self.get_data_recursive(root.right, data)
                if bool == True:
                    return bool
                else:
                    return (self.get_data_recursive(root.left, data))

    def get_data_nonrecursive(self,root,data):
        """Hierarchical traversal"""
        if root is None:
            return None
        else:

            node_array = [root]
            bool = True
            if data == root.data:
                return bool
            else:
                while node_array != []:
                    pop_node = node_array.pop(0)
                    if pop_node.left is not None:
                        node_array.append(pop_node.left)
                        if pop_node.left.data == data:
                            return bool

                    if pop_node.right is not None:
                        node_array.append(pop_node.right)
                        if pop_node.right.data == data:
                            return bool

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(100):
        t.add(i)

    m=GetData(t)
    print(m.get_data_recursive(t.root,11))
    print(m.get_data_nonrecursive(t.root,11))
