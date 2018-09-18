#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from tree_category.binary_tree import BinaryTree

class GetMaxLevel(object):
    def __init__(self,tree):
        self.tree = tree

    def get_max_level(self):
        cur_sum = 0
        max_sum = 0
        level = 0
        max_level = 0
        if self.tree.root is None:
            return None
        else:
            node_array = [self.tree.root]
            while node_array != []:
                pop_node = node_array.pop(0)
                if node_array == []:
                    if(cur_sum >= max_sum):
                        max_sum = cur_sum
                        max_level = level

                    cur_sum = 0

                    if node_array != []:
                        node_array.append(None)
                    level += 1
                else:
                    cur_sum += pop_node.data
                    if pop_node.left is not None:
                        node_array.append(pop_node.left)

                    if pop_node.right is not None:
                        node_array.append(pop_node.right)

        return max_level

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetMaxLevel(t)
    print(m.get_max_level())


