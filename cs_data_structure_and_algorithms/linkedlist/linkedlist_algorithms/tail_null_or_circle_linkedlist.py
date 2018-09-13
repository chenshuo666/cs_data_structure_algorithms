#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class TailNullOrCircle(object):
    def __init__(self, linkedlist):
        self.linkedlist = linkedlist

    def judge(self):
        if self.linkedlist.head == None:
            return False

        first_index = self.linkedlist.head
        second_index = self.linkedlist.head

        while first_index.next != None and second_index.next.next != None:
            first_index = first_index.next
            second_index = second_index.next.next
            if first_index == second_index:
                return True
        return False

if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    t1.travel_print()
    m = TailNullOrCircle(t1)
    print(m.judge())
