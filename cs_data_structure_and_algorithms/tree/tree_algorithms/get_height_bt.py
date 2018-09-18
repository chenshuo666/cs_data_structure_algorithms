#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from tree_category.binary_tree import BinaryTree

class GetHeight(object):
    def __init__(self,tree):
        self.tree = tree

    def get_height_recursive(self,root):
        if root is None:
            return 0
        else:
            leftheight = self.get_height_recursive(root.left)
            rightheight = self.get_height_recursive(root.right)
        if (leftheight > rightheight):
            return (leftheight+1)
        else:
            return (rightheight+1)

    def get_height_nonrecursive(self):
        if self.tree.root is None:
            return None
        else:
            node_array=[self.tree.root]
            val=[]
            while node_array:
                val.append([x.data for x in node_array])
                pop_node=[]
                for i in node_array:
                    if i.left:
                        pop_node.append(i.left)
                    if i.right:
                        pop_node.append(i.right)
                node_array = pop_node
            return len(val)

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetHeight(t)
    print(m.get_height_nonrecursive())
