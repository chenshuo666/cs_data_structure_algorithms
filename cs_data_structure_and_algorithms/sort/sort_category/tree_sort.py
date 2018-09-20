#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeSort:
    def __init__(self):
        self.root = None

    def search(self, root, parent, data):
        if root is None:
            return False, root, parent
        if root.data == data:
            return True, root, parent
        if root.data > data:
            return self.search(root.left, root, data)
        else:
            return self.search(root.right, root, data)

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node

        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            if data > p.data:
                p.right = node
            else:
                p.left = node

    def sort(self, root):
        if root is None:
            return []
        result = [root.data]
        left_data = self.sort(root.left)
        right_data = self.sort(root.right)
        return left_data + result + right_data

if __name__ == '__main__':

    t = TreeSort()
    mm=[23,34,2,1,235,5,765,86,59,760,235,456,123,32346,347]
    for i in range(len(mm)):
        t.insert(mm[i])
    print(t.sort(t.root))
