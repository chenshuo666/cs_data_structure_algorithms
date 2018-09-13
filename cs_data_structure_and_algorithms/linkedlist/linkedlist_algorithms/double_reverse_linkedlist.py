#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList,Node

class DoubleReverse():
    def __init__(self,linkedlist,likedlist1):
        self.linkedlist = linkedlist
        self.likedlist1 = likedlist1
        self.record = []

    def reverse(self):
        i=1
        head = self.linkedlist.head
        if head == None:
            return -1
        elif head.next == None:
            return -1
        else:
            if (self.linkedlist.length) % 2 ==0:
                while i <= int(self.linkedlist.length/2):
                    self.likedlist1.insert_append(head.next.data)
                    self.likedlist1.insert_append(head.data)
                    head = head.next.next
                    i+=1
            else:
                while i <= int(self.linkedlist.length/2):
                    self.likedlist1.insert_append(head.next.data)
                    self.likedlist1.insert_append(head.data)
                    if head.next.next.next == None:
                        self.likedlist1.insert_append(head.next.next.data)
                    head = head.next.next
                    i+=1

if __name__ == '__main__':
    t = SinglyLinkedList()
    t1 = SinglyLinkedList()
    for i in range(11):
        t.insert_append(i)
    t.travel_print()
    m = DoubleReverse(t,t1)
    m.reverse()
    t1.travel_print()