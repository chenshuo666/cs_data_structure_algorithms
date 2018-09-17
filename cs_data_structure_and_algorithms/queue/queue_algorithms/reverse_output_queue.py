#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class ReverseOutputQueue():
    def __init__(self,queue,stack):
        self.queue = queue
        self.stack = stack

    def reverse(self):
        if self.queue.isEmpty != True:
            for i in range(self.queue.length):
                self.stack.push(self.queue.dequeue())

        return self.stack