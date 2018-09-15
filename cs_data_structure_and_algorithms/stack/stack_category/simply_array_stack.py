#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class SimplyArrayStack:
    def __init__(self,max_capacity):
        self.max_capacity = max_capacity
        self.top=None #初始化最开始的位置
        self.items = []
        self.length = 0

    def get_top(self):  #获取栈顶的元素
        return self.items[-1]

    def size(self):
        """获取栈的大小"""
        return self.length

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def isStackFull(self):
        if self.size()==self.max_capacity:
            return True
        else:
            return False

    def push(self, data):
        if self.isStackFull() :
            print("the stack is full")
        else:
            self.items.append(data)
            self.top = self.items[-1]
            self.length += 1

    def pop(self):
        out = self.items[self.length-1]
        self.length -= 1
        return out

    def travel_print(self):
        """
        遍历整个栈，并输出栈的值
        """
        length = int(self.length)

        if self.isEmpty():
            print("Stack's length is 0")
        else:
            print("top -->", self.items[length-1],end =' ')
            length = length - 2
            while length!=-1:
                print("-->", self.items[length], end =' ')
                length = length-1
            print(" ")

    def clear_simply_array_stack(self):
        self.top = None
        self.length = 0
        print("the stack is empty")
