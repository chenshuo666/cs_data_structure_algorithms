#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import math
class AdjacentContinueQueue():
    def __init__(self,queue,stack):
        self.queue = queue
        self.stack = stack

    def judge(self):
        global  judge
        judge = True
        while self.stack.isEmpty() !=True:
            self.queue.enqueue(self.stack.pop())

        while self.queue.isEmpty() !=True:
            self.stack.push(self.queue.dequeue())

        while self.stack.isEmpty() != True:
            n = self.stack.pop()
            self.queue.enqueue(n)
            if self.stack.isEmpty() != True:
                m = self.stack.pop()
                self.queue.enqueue(m)
                if abs(n-m) !=1:
                    judge = False

        while self.queue.isEmpty() != True:
            self.stack.push(self.queue.dequeue())

        return judge

