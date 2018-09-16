#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from stack_category.simply_array_stack import SimplyArrayStack


class PalindromeStack(object):
    def __init__(self,stack,stack1):
        self.stack = stack
        self.stack1 = stack1

    def judge(self,str):
        i = 0
        len_str = int(len(str)/2)
        while i < len(str):
            self.stack.push(str[i])
            i+=1
        j = 0
        while j < len_str:
            self.stack.push(self.stack.pop())
            j+=1

        if len(str) % 2 ==0:
            n = 0
            while n < len_str:
                if self.stack.pop() != self.stack.pop():
                    return 0
            return 1
        else :
            self.stack.pop()
            n = 0
            while n < len_str:
                if self.stack.pop() != self.stack.pop():
                    return 0
            return 1




