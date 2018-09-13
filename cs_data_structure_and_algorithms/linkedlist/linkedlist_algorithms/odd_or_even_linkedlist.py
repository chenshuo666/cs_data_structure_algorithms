#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class OddOrEven():
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist

    def judge(self):
        cur = self.linkedlist.head
        while cur != None and cur.next != None:
            cur = cur.next.next
        if cur == None:
            return 1
        return 0

if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()
    m = OddOrEven(t1)
    print(m.judge())
