#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class FindModNode():

    def __init__(self,linkedlist,n):
        self.n = n
        self.linkedlist = linkedlist
        self.record = []

    def find(self):
        cur = self.linkedlist.head
        while cur:
            if cur.data % self.n == 0:
                self.record.append(cur.data)
            cur = cur.next
        i = self.record[-1]
        return i

if __name__ == '__main__':
    t = SinglyLinkedList()
    for i in range(100):
        t.insert_append(i)
    t.travel_print()

    m = FindModNode(t,3)
    print(m.find())



