#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
from stack_category.simply_array_stack import SimplyArrayStack

class SpanStack(object):
    def __init__(self, stack):
        self.stack = stack

    def get_span(self):
        spans = []
        for i in range(self.stack.length):
            m = 1
            j = i-1
            while j >0 and self.stack.items[j] <= self.stack.items[j+1]:
                m+=1
                j-=1
            spans[i] = m
        return spans


