#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from stack_category.simply_array_stack import SimplyArrayStack

class UpSortStack(object):
    def __init__(self, stack,stack1):
        self.stack = stack
        self.stack1 = stack1

    def sort(self):
        a = sorted(self.stack.items)
        for i in range(len(a)):
            self.stack1.push(a[i])
        return self.stack1

if __name__ == "__main__":
    t1 = SimplyArrayStack(20)
    t2 = SimplyArrayStack(20)
    a = [1,3,5,67,354,57,54,2,4,6,568,876,85556,7]
    for i in range(len(a)):
        t1.push(a[i])

    m = UpSortStack(t1,t2)

    m.sort().travel_print()