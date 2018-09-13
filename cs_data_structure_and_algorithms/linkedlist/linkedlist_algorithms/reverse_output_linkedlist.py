#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class ReverseOutputLinkedlist():
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist
        self.record  = []

    def print_tial(self,head):
        if head == None:
            return -1
        self.print_tial(head.next)
        self.record.append(head.data)


if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()

    m = ReverseOutputLinkedlist(t1)
    m.print_tial(t1.head)
    print(m.record)
