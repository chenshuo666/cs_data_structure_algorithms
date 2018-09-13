#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class PalidromeLinkedlist():
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist
        self.record = []

    def judge(self):
        cur = self.linkedlist.head
        if cur == None:
            return
        elif cur.next == None:
            return
        else:
            i = 0
            while i < self.linkedlist.length:
                self.record.append(cur.data)
                cur = cur.next

if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()
    m =PalidromeLinkedlist(t1)
    m.judge()

    print(m.record)
