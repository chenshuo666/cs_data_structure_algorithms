#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class MergeTwoSored(object):
    def __init__(self,linkedlist,linkedlist1,linkedlist2):
        self.linkedlist = linkedlist
        self.linkedlist1 = linkedlist1
        self.linkedlist2 = linkedlist2
        self.record = []

    def merge(self, a, b):
        global result

        while a.data <= b.data and a != None:
            result = a
            self.linkedlist2.insert_append(result.data)
            a = a.next

        while a.data > b.data and b != None:
            result = b
            self.linkedlist2.insert_append(result.data)
            b=b.next




if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()
    a=[0,1,2,3,5,3456,567585,867896789,78908435232]
    t2 =SinglyLinkedList()
    for i in range(len(a)):
        t2.insert_append(a[i])
    t2.travel_print()
    print(t2.head.data)

    t3 = SinglyLinkedList()

    m=MergeTwoSored(t1,t2,t3)
    m.merge(t1.head , t2.head)
    t3.travel_print()

