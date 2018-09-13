#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class Node(object):
    """One-way circular list node"""

    def __init__(self, data):
        self.data = data
        self.next = None

class JosephRing(object):
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist

    def get_last(self,m):
        cur=self.linkedlist.head
        cur_change = self.linkedlist.head
        while cur.next:
            cur = cur.next
        cur.next = cur_change           

        t=self.linkedlist.length
        while t >1 :
            for i  in range(m-1):
                cur = cur.next
            cur.next = cur.next.next
            t-=1

        return cur.data

if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(56):
        t1.insert_append(i)


    m = JosephRing(t1)
    print(m.get_last(2))








