#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.double_linkedlist import DoubleLinkList

class PalidromeLinkedlist():
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist
        self.record = []

    def judge(self):
        i = 0
        j = self.linkedlist.get_length()
        cur = self.linkedlist.head
        head_node = self.linkedlist.head
        while cur.next:
            cur = cur.next
        while i < j and cur.data == head_node.data:
            i+=1
            j-=1
            head_node = head_node.next
            cur = cur.prev

        if i < j:
            return 0
        else:
            return 1

if __name__ == '__main__':
    t1 = DoubleLinkList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()
    m =PalidromeLinkedlist(t1)
    print(m.judge())
