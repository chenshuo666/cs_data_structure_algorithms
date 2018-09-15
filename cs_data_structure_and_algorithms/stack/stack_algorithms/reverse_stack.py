#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from stack_category.linkedlist_stack import LinkedListStack

class ReverseStack(object):
    def __init__(self,stack):
        self.stack = stack

    def reverse(self,stack):
        if stack.isEmpty():
            return
        temp = stack.pop()
        self.reverse(stack)
        self.insert(stack,temp)

    def insert(self,stack,data):
        if stack.isEmpty():
            stack.push(data)
            return
        temp = stack.pop()
        self.insert(stack,data)
        stack.push(temp)

if __name__ =="__main__":
    t= LinkedListStack(20)
    for i in range(10):
        t.push(i)

    t.travel_print()

    m = ReverseStack(t)
    m.reverse(t)
    t.travel_print()