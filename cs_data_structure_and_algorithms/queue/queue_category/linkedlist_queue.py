#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node(object):
    # node
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue():

    def __init__(self,max_capacity):
        self.max_capacity = max_capacity
        self.front = Node()
        self.rear = Node()
        self.length = 0

    def get_length(self):
        return self.length

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def isQueueFull(self):
        if self.get_length()==self.max_capacity:
            return True
        else:
            return False

    def enqueue(self, data):
        #
        node = Node(data)
        if self.isEmpty():
            self.front = node
            self.rear = node
            self.length +=1
        else:
            if self.isQueueFull():
                print("queue is full!")
            else:
                self.rear.next = node
                self.rear = node
                self.length += 1

    def dequeue(self):
        #
        if self.isEmpty():
            raise ValueError("queue is empty!")
        else:
            out_data = self.front.data
            self.front = self.front.next
            self.length -= 1
            return out_data

    def travel_print(self):
        a = []
        if self.isEmpty():
            print("queue is empty!")
        j = self.length
        node = self.front
        while j > 0:
            a.append(node.data)
            node = node.next
            j -= 1
        return a



