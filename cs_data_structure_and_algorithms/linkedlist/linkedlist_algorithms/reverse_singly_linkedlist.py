#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ReverseSinglyLinkedlist():
    def __init__(self,linkedlist,linkedlist1):
        self.linkedlist = linkedlist
        self.linkedlist1 = linkedlist1

    def reverse(self):
        cur = self.linkedlist.head
        if self.linkedlist.head is None:
            return -1
        else:
            for i in range(self.linkedlist.length):
                self.linkedlist1.insert_head(cur.data)
                cur = cur.next

        return self.linkedlist1

if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()

    t2 =SinglyLinkedList()

    m=ReverseSinglyLinkedlist(t1,t2)

    m.reverse().travel_print()


