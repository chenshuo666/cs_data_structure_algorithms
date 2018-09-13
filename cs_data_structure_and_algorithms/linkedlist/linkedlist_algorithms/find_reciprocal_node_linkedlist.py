#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from likedlist_category.singly_linkedlist import SinglyLinkedList

class FindReciprocalNode():

    def __init__(self,linkedlist,length,n):
        self.n = n
        self.linkedlist = linkedlist
        self.length = length

    def get_n_node(self):
        return self.linkedlist.get_data_by_index(int(self.length - self.n))

    def get_n_node_by_two_index(self):
        pass

if __name__ == '__main__':
    t = SinglyLinkedList()
    for i in range(10):
        t.insert_append(i)
    t.travel_print()

    m=FindReciprocalNode(t,t.get_length(),4)
    print(m.get_n_node())