#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))

from tree_category.binary_tree import BinaryTree


class GetHelfNodeNum(object):
    def __init__(self, tree):
        self.tree = tree

    def get_helf_node_num(self):
        count = 0
        if self.tree.root is None:
            return None
        else:
            node_array = [self.tree.root]
            while node_array != []:
                pop_node = node_array.pop(0)
                if (pop_node.left is not None and pop_node.right is  None)\
                        or (pop_node.left is None and pop_node.right is not None):
                    count += 1

                if pop_node.left is not None:
                    node_array.append(pop_node.left)

                if pop_node.right is not None:
                    node_array.append(pop_node.right)
        return count


if __name__ == "__main__":
    t = BinaryTree()
    for i in range(10):
        t.add(i)

    m = GetHelfNodeNum(t)
    print(m.get_helf_node_num())

