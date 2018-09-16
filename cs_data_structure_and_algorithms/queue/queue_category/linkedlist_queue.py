#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node(object):
    # 节点
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

    def enQueue(self, data):
        # 入队
        node = Node(data)
        if self.isEmpty():
            self.front = node
            self.rear = node
            self.length +=1
        else:
            if self.isQueueFull():
                print("Queue is full!")
            else:
                self.rear.next = node
                self.rear = node
                self.length += 1

    def deQueue(self):
        # 出队
        if self.isEmpty():
            raise ValueError("Queue is empty!")
        else:
            out_data = self.front.data
            self.front = self.front.next
            self.length -= 1
            return out_data

    def travel_print(self):

        if self.isEmpty():
            print("Queue is empty!")
        j = self.length
        node = self.front
        while j > 0:
            print(node.data)
            node = node.next
            j -= 1
        print('')



