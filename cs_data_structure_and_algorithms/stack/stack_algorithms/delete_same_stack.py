#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from stack_category.simply_array_stack import SimplyArrayStack

class DeleteSameStack(object):
    def __init__(self, stack):
        self.stack = stack

    def del_repeatnum(self):
        s = []
        for i in self.stack.items:
            print(i)
            if i not in s:
                s.append(i)
            else:
                pass
        return sorted(s)

if __name__ == "__main__":
    t1 = SimplyArrayStack(20)
    a = [1,3,5,67,89,0,4,5,6,7,8,6,24,55,45]
    for i in range(len(a)):
        t1.push(a[i])
    m = DeleteSameStack(t1)
    print(m.del_repeatnum())

