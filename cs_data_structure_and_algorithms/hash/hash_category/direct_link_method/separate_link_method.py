#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SeparateLinkMethod(object):
    def __init__(self, tableSize):
        self.table = [None] * tableSize
        self.num_node = 0  # number of nodes in the map

    def __len__(self):
        return self.num_node

    def hash_get_index(self, value):
        return abs(hash(value)) % len(self.table)

    def get_item(self, value):
        j = self.hash_get_index(value)
        node = self.table[j]
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            raise KeyError('valueError' + repr(value))
        return node

    def insert(self, value):

        node_insert = ListNode(value)
        if value is None:
            return

        j = int(self.hash_get_index(value))  # type: int
        node = self.table[j]

        self.table[j] = node_insert
        self.table[j].next = node
        self.num_node += 1

    def delete(self, value):
        j = self.hash_get_index(value)
        node = self.table[j]

        if node is not None:
            if node.value == value:
                self.table[j] = node.next
                self.num_node -= 1
            else:
                while node.next != None:
                    pre = node
                    node = node.next
                    if node.value == value:
                        pre.next = node.next
                        self.num_node -= 1
                        break


if __name__ == "__main__":
    t = SeparateLinkMethod(10)
    print(t.hash_get_index(48))
    t.insert(48)
    print(t.get_item(48))
    #