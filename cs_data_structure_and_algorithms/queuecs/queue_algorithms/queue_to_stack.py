#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))))

from queue_category.simply_array_queue import SimplyArrayQueue
from stack.stack_category.linkedlist_stack import LinkedListStack

class QueueToStack():
    def __init__(self,queue,stack,stack1):
        self.queue = queue
        self.stack = stack
        self.stack1 = stack1

    def queue_to_stack(self):
        if self.queue.isEmpty != True:
            for i in range(self.queue.length):
                self.stack.push(self.queue.dequeue())

        for i in range(self.stack.length):
            self.stack1.push(self.stack.pop())

        return self.stack1