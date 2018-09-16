#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class SimplyArrayQueue():

    def __init__(self, max_capacity):
        self.data = list(None for _ in range(max_capacity + 1))
        self.maxsize = max_capacity + 1
        self.front = 0
        self.rear = 0
        self.length = 0

    def get_length(self):
        return self.length

    def isQueueFull(self):
        if (self.rear + 1) % self.maxsize == self.front:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def enqueue(self, data):

        if self.isQueueFull():
            print("Queue is full!")
        else:
            self.data[self.rear] = data
            self.rear = (self.rear + 1) % self.maxsize
            self.length += 1

    def dequeue(self):

        if self.isEmpty():
            print("Queue is empty!")
        else:
            out_data = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            self.length -= 1
            return out_data

    def travel_print(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            j = self.front
            print('front:')
            while j != self.rear:
                print(self.data[j])
                j = (j + 1) % self.maxsize
            print('')

    def clear_array_queue(self):
        self.rear = -1
        self.front = -1

