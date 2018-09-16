#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from stack_category.simply_array_stack import SimplyArrayStack

class AdjacentNumberStack(object):
    def __init__(self, stack, stack1):
        self.stack = stack
        self.stack1 = stack1
         
    def delete_adjacent_number(self):
        t=-1
        i=0
        while i < len(self.stack.items):
            if t == -1 or self.stack.items[t] != self.stack.items[i]:
                t+=1
                self.stack.items[t] = self.stack.items[i]
                i+=1
            else:
                while i < len(self.stack.items) and self.stack.items[t] == self.stack.items[i]:
                    i+=1
                t-=1
        return t+1
    
    def get_new_stack(self):
        index = self.delete_adjacent_number()
        for i in range(index):
            self.stack1.push(self.stack.items[i])

        return self.stack1


if __name__ == "__main__":
    t1 = SimplyArrayStack(20)
    t2 = SimplyArrayStack(20)
    a = [1, 67, 5, 5, 67, 354, 54, 54, 2, 2, 2, 354, 876, 85556, 85556]
    for i in range(len(a)):
        t1.push(a[i])

    m = AdjacentNumberStack(t1,t2)
    m.get_new_stack().travel_print()






