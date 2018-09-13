#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class FindInnerNode():
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist

    def find_center1(self):
        p1 = self.linkedlist.head
        p2 = self.linkedlist.head
        i = 0
        while p1.next is not None:
            if i==0:
                p1 = p1.next
                i =1
            elif i == 1:
                p1 = p1.next
                p2 = p2.next
                i=0
        return p2.data

    def find_center2(self):
        cur = self.linkedlist.head
        i=0
        t = int(self.linkedlist.length/2)
        while i < t-1:
            cur = cur.next
            i+=1
        return cur.data


if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()
    m = FindInnerNode(t1)
    print(m.find_center1())
    print(m.find_center2())
