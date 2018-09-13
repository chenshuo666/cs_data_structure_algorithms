#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InsertSortedLinkedlist(object):
    def __init__(self,linkedlist):
        self.linkedlist = linkedlist
        
    def insert_up(self,value):

        global record
        this_node = Node(value)
        cur = self.linkedlist.head
        i = 1
        if self.linkedlist.head is None:
            self.linkedlist.head = this_node

        else:
            while i <= self.linkedlist.length:
                if cur.data < value:
                    record = cur
                    cur = cur.next
                    if i == self.linkedlist.length:
                        record.next = this_node
                        break
                else:
                    record.next = this_node
                    this_node.next = cur
                    break
                i +=1

    def insert_down(self, value):

        global record
        this_node = Node(value)
        cur = self.linkedlist.head
        i = 1
        if self.linkedlist.head is None:
            self.linkedlist.head = this_node

        else:
            while i <= self.linkedlist.length:
                if cur.data > value:
                    record = cur
                    cur = cur.next
                    if i == self.linkedlist.length:
                        record.next = this_node
                        break
                else:
                    record.next = this_node
                    this_node.next = cur
                    break
                i += 1
