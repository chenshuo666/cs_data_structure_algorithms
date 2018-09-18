#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))
from stack.stack_category.linkedlist_stack import LinkedListStack


class TwoStackQueue(object):

    def __init__(self):
        self.stack1 = LinkedListStack(10)
        self.stack2 = LinkedListStack(10)
        self.length = 0

    def get_length(self):
        return self.length

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def enqueue(self, data):

        self.stack1.push(data)
        self.length += 1

    def dequeue(self):
        if (self.stack2.isEmpty() == True):
            while (not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.get_top())
                self.stack1.pop()
            self.stack2.pop()
            self.length -= 1
        else:
            self.stack2.pop()
            self.length -= 1

    def get_top(self):
        if (self.stack2.isEmpty() == True):
            while (not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.get_top())
                self.stack1.pop()
            return self.stack2.get_top()
        else:
            return self.stack2.get_top()

if __name__ == "__main__":
    l1=TwoStackQueue()
    l1.enqueue(10)
    l1.enqueue(20)
    l1.enqueue(30)
    l1.enqueue(40)
    l1.enqueue(50)
    l1.stack1.travel_print()
    print(l1.get_top())

    # print(l1.dequeue())
